"""CLI 진입점 — 노드 스크리너.

Usage:
    python3 cli.py phase0-test          # Phase 0 왕복 테스트
    python3 cli.py ingest               # Phase 1 시드 인제스트
    python3 cli.py ingest --seed-dir /path
    python3 cli.py stats hbm 2026-07    # 그래프 통계 출력
    python3 cli.py coverage-check       # L2 커버리지 갭 확인
    python3 cli.py integrity-check hbm 2026-07  # L3 무결성 검사
    python3 cli.py import-csv --chain hbm --companies c.csv --edges e.csv
    python3 cli.py score hbm 2026-07        # 스코어 산출 + 랭킹 출력
    python3 cli.py calibrate hbm 2026-07    # L4 캘리브레이션 루프
"""

from __future__ import annotations

import sys
from pathlib import Path

# 프로젝트 루트를 sys.path에 추가
PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def cmd_phase0_test() -> None:
    """Phase 0 왕복 테스트 실행."""
    import subprocess

    result = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/", "-v"],
        cwd=str(PROJECT_ROOT),
    )
    sys.exit(result.returncode)


def cmd_ingest(args: list) -> None:
    """Phase 1 시드 인제스트."""
    from src.ingest import ingest_seed
    from src.graph_io import save_graph
    from src.report import pass_rate_report, graph_stats, coverage_report

    seed_dir = None
    model = "claude-sonnet-4-6"
    year_month = "2026-07"
    offline_dir = None

    # 인자 파싱
    i = 0
    while i < len(args):
        if args[i] == "--seed-dir" and i + 1 < len(args):
            seed_dir = args[i + 1]
            i += 2
        elif args[i] == "--model" and i + 1 < len(args):
            model = args[i + 1]
            i += 2
        elif args[i] == "--year-month" and i + 1 < len(args):
            year_month = args[i + 1]
            i += 2
        elif args[i] == "--offline-dir" and i + 1 < len(args):
            offline_dir = args[i + 1]
            i += 2
        else:
            i += 1

    # 인제스트 실행
    chain_graphs, results = ingest_seed(
        seed_dir=seed_dir, model=model, year_month=year_month,
        offline_dir=offline_dir,
    )

    if not chain_graphs:
        print("[ERROR] 추출 결과 없음")
        sys.exit(1)

    # 그래프 저장
    print("=" * 60)
    print("그래프 저장")
    print("=" * 60)
    for chain, graph in chain_graphs.items():
        path = save_graph(graph, chain, year_month)
        print(f"  {chain}: {path}")

    # L1 리포트
    print("\n" + "=" * 60)
    report = pass_rate_report(results)
    print(report)

    # 체인별 통계
    for chain, graph in chain_graphs.items():
        print("\n" + "=" * 60)
        print(graph_stats(graph))

    # L2 커버리지 (자동 실행)
    print("\n" + "=" * 60)
    coverage = coverage_report(chain_graphs)
    print(coverage)

    # PROGRESS.md에 결과 추가
    progress_path = PROJECT_ROOT / "PROGRESS.md"
    if progress_path.exists():
        existing = progress_path.read_text(encoding="utf-8")
    else:
        existing = ""

    appendix = f"\n\n---\n\n### L1 인제스트 결과 (자동 기록)\n\n{report}"
    for chain, graph in chain_graphs.items():
        appendix += f"\n\n{graph_stats(graph)}"
    appendix += f"\n\n{coverage}"

    progress_path.write_text(existing + appendix, encoding="utf-8")
    print(f"\n[INFO] 결과가 PROGRESS.md에 기록되었습니다.")


def cmd_stats(args: list) -> None:
    """그래프 통계 출력."""
    if len(args) < 2:
        print("Usage: python3 cli.py stats <chain> <year-month>")
        print("Example: python3 cli.py stats hbm 2026-07")
        sys.exit(1)

    chain = args[0]
    year_month = args[1]

    from src.graph_io import load_graph
    from src.report import graph_stats

    try:
        graph = load_graph(chain, year_month)
    except FileNotFoundError:
        print(f"[ERROR] 그래프 파일 없음: graph/{chain}/{year_month}.json")
        sys.exit(1)

    print(graph_stats(graph))


def cmd_coverage_check(args: list) -> None:
    """L2 커버리지 갭 확인."""
    from src.graph_io import load_graph, GRAPH_DIR
    from src.report import coverage_report

    chain_graphs = {}
    for chain_dir in GRAPH_DIR.iterdir():
        if chain_dir.is_dir():
            for json_file in sorted(chain_dir.glob("*.json")):
                ym = json_file.stem
                graph = load_graph(chain_dir.name, ym)
                chain_graphs[chain_dir.name] = graph

    if not chain_graphs:
        print("[ERROR] 저장된 그래프 없음. 먼저 ingest를 실행하세요.")
        sys.exit(1)

    gt_path = args[0] if args else None
    print(coverage_report(chain_graphs, gt_path))


def cmd_integrity_check(args: list) -> None:
    """L3 무결성 검사."""
    if len(args) < 2:
        print("Usage: python3 cli.py integrity-check <chain> <year-month>")
        sys.exit(1)

    chain = args[0]
    year_month = args[1]

    from src.graph_io import load_graph
    from src.report import integrity_report

    try:
        graph = load_graph(chain, year_month)
    except FileNotFoundError:
        print(f"[ERROR] 그래프 파일 없음: graph/{chain}/{year_month}.json")
        sys.exit(1)

    print(integrity_report(graph))


def cmd_import_csv(args: list) -> None:
    """CSV에서 그래프 데이터 임포트."""
    chain = None
    companies_csv = None
    edges_csv = None
    year_month = "2026-07"

    i = 0
    while i < len(args):
        if args[i] == "--chain" and i + 1 < len(args):
            chain = args[i + 1]
            i += 2
        elif args[i] == "--companies" and i + 1 < len(args):
            companies_csv = args[i + 1]
            i += 2
        elif args[i] == "--edges" and i + 1 < len(args):
            edges_csv = args[i + 1]
            i += 2
        elif args[i] == "--year-month" and i + 1 < len(args):
            year_month = args[i + 1]
            i += 2
        else:
            i += 1

    if not chain:
        print("Usage: python3 cli.py import-csv --chain hbm --companies c.csv --edges e.csv")
        sys.exit(1)

    from src.graph_io import load_graph, save_graph, import_companies_csv, import_edges_csv
    from src.models import Graph, GraphMeta

    # 기존 그래프 로드 또는 새로 생성
    try:
        graph = load_graph(chain, year_month)
        print(f"[INFO] 기존 그래프 로드: {chain}/{year_month}")
    except FileNotFoundError:
        graph = Graph(meta=GraphMeta(chain=chain, year_month=year_month))
        print(f"[INFO] 새 그래프 생성: {chain}/{year_month}")

    if companies_csv:
        graph = import_companies_csv(graph, companies_csv)
        print(f"[INFO] 기업 임포트: {companies_csv}")

    if edges_csv:
        graph = import_edges_csv(graph, edges_csv)
        print(f"[INFO] 엣지 임포트: {edges_csv}")

    path = save_graph(graph, chain, year_month)
    print(f"[INFO] 저장: {path}")


def cmd_score(args: list) -> None:
    """스코어 산출 + 랭킹 출력."""
    if len(args) < 2:
        print("Usage: python3 cli.py score <chain> <year-month>")
        print("Example: python3 cli.py score hbm 2026-07")
        sys.exit(1)

    chain = args[0]
    year_month = args[1]

    from src.graph_io import load_graph
    from src.scoring import score_functions, score_companies
    from src.report import score_report

    try:
        graph = load_graph(chain, year_month)
    except FileNotFoundError:
        print(f"[ERROR] 그래프 파일 없음: graph/{chain}/{year_month}.json")
        sys.exit(1)

    fn_scores = score_functions(graph)
    co_scores = score_companies(graph, fn_scores)
    print(score_report(fn_scores, co_scores))


def cmd_calibrate(args: list) -> None:
    """L4 캘리브레이션 루프."""
    if len(args) < 2:
        print("Usage: python3 cli.py calibrate <chain> <year-month>")
        print("Example: python3 cli.py calibrate hbm 2026-07")
        sys.exit(1)

    chain = args[0]
    year_month = args[1]

    from src.graph_io import load_graph
    from src.scoring import load_weights, save_weights
    from src.calibrate import load_ground_truth, calibration_loop
    from src.report import calibration_report

    try:
        graph = load_graph(chain, year_month)
    except FileNotFoundError:
        print(f"[ERROR] 그래프 파일 없음: graph/{chain}/{year_month}.json")
        sys.exit(1)

    gt = load_ground_truth(chain)
    if not gt:
        print(f"[ERROR] ground_truth.yaml에 {chain} 노드 없음")
        sys.exit(1)

    weights = load_weights()
    result = calibration_loop(graph, gt, weights)

    print(calibration_report(result))

    # 결과를 weights.yaml에 저장
    from datetime import datetime

    save_weights(result["final_weights"], {
        "last_run": datetime.now().isoformat(),
        "chain": chain,
        "recall_at_20": round(result["recall"], 3),
        "mean_rank_pct": round(result["mean_rank_pct"], 3),
        "converged": result["converged"],
    })
    print(f"\n[INFO] 최종 가중치가 config/weights.yaml에 저장되었습니다.")

    # PROGRESS.md에 기록
    progress_path = PROJECT_ROOT / "PROGRESS.md"
    existing = progress_path.read_text(encoding="utf-8") if progress_path.exists() else ""
    appendix = f"\n\n---\n\n### L4 캘리브레이션 결과 ({chain}, 자동 기록)\n\n"
    appendix += calibration_report(result)
    progress_path.write_text(existing + appendix, encoding="utf-8")
    print(f"[INFO] 결과가 PROGRESS.md에 기록되었습니다.")


def cmd_report(args: list) -> None:
    """HTML 스코어보드 리포트 생성."""
    if len(args) < 2:
        print("Usage: python3 cli.py report <chain> <year-month> [--output-dir /path]")
        print("Example: python3 cli.py report hbm 2026-07")
        sys.exit(1)

    chain = args[0]
    year_month = args[1]
    output_dir = None

    i = 2
    while i < len(args):
        if args[i] == "--output-dir" and i + 1 < len(args):
            output_dir = args[i + 1]
            i += 2
        else:
            i += 1

    from src.graph_io import load_graph
    from src.html_report import generate_scoreboard

    try:
        graph = load_graph(chain, year_month)
    except FileNotFoundError:
        print(f"[ERROR] 그래프 파일 없음: graph/{chain}/{year_month}.json")
        sys.exit(1)

    path = generate_scoreboard(graph, chain, year_month, output_dir)
    print(f"[OK] 스코어보드 생성: {path}")


COMMANDS = {
    "phase0-test": (cmd_phase0_test, "Phase 0 왕복 테스트"),
    "ingest": (cmd_ingest, "Phase 1 시드 인제스트"),
    "stats": (cmd_stats, "그래프 통계 출력"),
    "coverage-check": (cmd_coverage_check, "L2 커버리지 갭 확인"),
    "integrity-check": (cmd_integrity_check, "L3 무결성 검사"),
    "import-csv": (cmd_import_csv, "CSV 임포트"),
    "score": (cmd_score, "스코어 산출 + 랭킹"),
    "calibrate": (cmd_calibrate, "L4 캘리브레이션 루프"),
    "report": (cmd_report, "HTML 스코어보드 리포트 생성"),
}


def main() -> None:
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print("불가결 노드 스크리너 CLI\n")
        print("Commands:")
        for name, (_, desc) in COMMANDS.items():
            print(f"  {name:20s} {desc}")
        print("\nRun 'python3 cli.py <command> --help' for details.")
        sys.exit(0)

    cmd_name = sys.argv[1]
    cmd_args = sys.argv[2:]

    if cmd_name not in COMMANDS:
        print(f"[ERROR] 알 수 없는 명령: {cmd_name}")
        print(f"사용 가능: {', '.join(COMMANDS.keys())}")
        sys.exit(1)

    handler, _ = COMMANDS[cmd_name]

    if cmd_name == "phase0-test":
        handler()
    else:
        handler(cmd_args)


if __name__ == "__main__":
    main()
