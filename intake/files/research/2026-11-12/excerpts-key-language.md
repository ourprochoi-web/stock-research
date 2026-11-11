> 조문 발췌. Lead 판단이 아니다. 라우팅은 brain/routing.jsonl.

# Key operative excerpts (as downloaded 2026-11-12)

Sources are official bill PDFs from GovInfo and the House Foreign Affairs Committee draft, plus Federal Register / eCFR / CRS. Line citations refer to the extracted `.txt` files in this folder.

## 1. AI OVERWATCH Act — H.R. 6875 IH (Dec 18, 2025) / House Foreign Affairs draft

Short title: “Artificial Intelligence Oversight of Verified Exports and Restrictions on Weaponizable Advanced Technology to Covered High-Risk Actors Act”.

30-day notice + joint-resolution block (House introduced text):

> Not fewer than 30 days prior to approving any license for the export, reexport, or in-country transfer of a covered integrated circuit to an entity that is located or headquartered in, or the ultimate parent company of which is headquartered in, a country of concern, the Under Secretary … shall submit to the appropriate congressional committees a copy of the license application…

> The license … may not be issued — (i) until the date that is not fewer than 30 days after the committees … received the certification …; and (ii) if Congress, prior to the date that is 30 days after such committees received such certification, enacts a joint resolution prohibiting the proposed export, reexport, or in-country transfer.

General licenses barred; prior licenses terminated; temporary denial until a national-security strategy is submitted.

Senate companion S. 4456 (Banks et al., Apr 30, 2026) keeps the 30-day certification (60 days if filed July 10–September 7) and the bar on issuing the license during that window, plus a standing denial for “restricted” chips (TPP of 21,000 or more). The introduced Senate text reviewed here does **not** include the House joint-resolution block.

## 2. Chip Security Act — H.R. 3447 IH (May 15, 2025)

> Not later than 180 days after the date of the enactment of this Act, the Secretary shall require any covered integrated circuit product to be outfitted with chip security mechanisms that implement location verification, using techniques that are feasible and appropriate on such date of enactment, before it is exported, reexported, or in-country transferred to or in a foreign country.

Notification if the product “is in a location other than the location specified,” “has been diverted to a user other than the user specified,” or has been tampered with (including efforts to “disable, spoof, manipulate, mislead or circumvent” the mechanisms).

Commerce may “verify, in a manner the Secretary determines appropriate, the ownership and location” of a covered product abroad, and keep a record of location and current end-user.

## 3. MATCH Act — H.R. 8170 IH (Apr 2, 2026)

Short title: “Multilateral Alignment of Technology Controls on Hardware Act”.

150-day allied-alignment clock, then U.S. jurisdiction if allies do not match:

> By the date that is 150 days after the date of the enactment of this Act, the covered agency heads shall jointly either— (A) certify … that all allied supplier countries have implemented— (i) countrywide controls … or other controls and licensing policies having the same practical effect; and (ii) license requirements for all applicable items, with a licensing policy of denial …; or (B) provide a list … of any allied supplier countries that have not implemented all controls…

> Unless the covered agency heads provide the certification in subparagraph (A), the covered agency heads shall issue regulations that— (A) establish U.S. jurisdiction over and apply countrywide controls to all covered semiconductor manufacturing equipment and components therefor exported from countries identified …

“Applicable item” includes a foreign-produced item that is a direct product of EAR-controlled software/technology (FDPR-style), a foreign-produced item “with more than zero percent de minimis controlled United States-origin content,” and a foreign-produced item containing ICs “presumptively designed or produced, directly or indirectly, with technology, software, or equipment that is subject to” the EAR.

“Countrywide controls” means licensing requirements and a policy of denial to any destination in a country of concern, **excluding** a fab that “existed as of the date of the enactment of this Act and remains owned and operated by a company headquartered, and having an ultimate parent headquartered, outside of any country of concern.”

“Allied supplier country” is defined functionally (not by a named list): any country that is not a country of concern and “is engaged in the production of covered semiconductor manufacturing equipment.”

One-time national-security waiver may extend the 150-day deadline by not more than 90 days.

## 4. Remote Access Security Act — H.R. 2683 EH (passed House Jan 12, 2026, 369–22)

> The term ‘remote access’ means access on a purposeful, knowing, reckless, or negligent basis to an item subject to the jurisdiction of the United States under this Act by a foreign person through a network connection, including the internet or a cloud computing service, from a location other than where the item is physically located if the Secretary determines that the use of the item could pose a serious risk to the national security or foreign policy of the United States.

The bill amends ECRA so that export-control authorities (licenses, penalties) also cover remote access. It does not itself write a customer-KYC rule; BIS would still have to issue regulations.

Senate companion S. 3519 (McCormick, Dec 17, 2025) is narrower: it targets remote access by a “foreign person of concern” via cloud IaaS, and lists specific high-risk uses (certain dual-use AI models, offensive cyber, certain surveillance).

## 5. H200 rule — 91 FR 1684 (Jan 15, 2026)

BIS changed the license review policy for certain chips (TPP < 21,000 and total DRAM bandwidth < 6,500 GB/s; e.g., NVIDIA H200, AMD MI325X) destined to end-users in China or Macau from presumption of denial to case-by-case, subject to certifications (U.S. supply, foundry-capacity, 50% cap vs U.S. end-use shipments, KYC / remote-access screening, U.S. third-party lab testing). Other D:5 / Macau-headquartered cases remain presumption of denial.

Separately, a Jan 14, 2026 presidential proclamation imposed a 25% Section 232 ad valorem tariff on certain advanced computing chips (including H200 and MI325X).

## 6. VEU revocation — 90 FR 42321 (effective Dec 31, 2025)

BIS removed Intel Semiconductor (Dalian) Ltd; Samsung China Semiconductor Co. Ltd; and SK hynix Semiconductor (China) Ltd from the China Validated End-User list.

## 7. Country Group D:5 (eCFR Supplement No. 1 to 15 CFR Part 740, as retrieved 2026-11-12)

D:5 (U.S. arms-embargoed) includes, among others: China (PRC), Russia, North Korea, Cuba, Burma (Myanmar), Iran, Iraq, Syria, Lebanon, Libya, Belarus, Venezuela, plus others (Afghanistan, CAR, DRC, Eritrea, Haiti, Nicaragua, Somalia, South Sudan, Sudan, Zimbabwe).

Vietnam is in D:1 and D:3, **not** D:5. Cambodia is in D:1 only on the current table (removed from D:5 as of a Feb 2026 revision, per contemporaneous commentary). Malaysia, Singapore, Indonesia, and Thailand are not in D:5 (they appear in Country Group B). Macau is in D:1/D:3/D:4, not D:5, but many advanced-computing rules treat Macau like China/D:5.

## 8. FY2027 NDAA status — CRS IN12704, updated Sep 1, 2026

House passed H.R. 8800 on July 22, 2026 (216–212). Senate cloture on the motion to proceed to S. 4784 failed July 14, 2026 (50–46). As of the CRS update, the Senate had taken no further floor steps. Later tracking (ndaa.ai and lame-duck previews) describes unofficial four-corners talks and a hoped-for December compromise; the bill was not enacted as of the mid-November 2026 sources reviewed for this memo.
