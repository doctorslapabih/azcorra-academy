import json, os
OUT = os.path.join(os.path.dirname(__file__), "..", "data", "lessons", "writing")
os.makedirs(OUT, exist_ok=True)
def T(md): return {"type": "text", "md": md}
def N(label, md): return {"type": "note", "label": label, "md": md}
def E(title, problem, steps, answer): return {"type": "example", "title": title, "problem": problem, "steps": steps, "answer": answer}
def MC(q, options, answer, why): return {"type": "mc", "q": q, "options": options, "answer": answer, "why": why}
L = []

L.append({"id": "subjects-verbs-and-complete-sentences", "title": "Subjects, verbs and complete sentences", "band": "Grade 7", "minutes": 14,
 "lede": "Every sentence needs three things. Find them and you can fix almost any sentence.",
 "sections": [
  T("## The three requirements\nA complete sentence has:\n\n1. A **subject**: who or what the sentence is about.\n2. A **verb**: what the subject does or is.\n3. A **complete thought**: it makes sense on its own.\n\n\"The driver delivered the load.\" Subject: the driver. Verb: delivered. Complete thought: yes."),
  T("## Find the verb first\nThe verb is the easiest piece to spot. Ask, \"What's happening?\" Then ask, \"Who or what is doing it?\" That's the subject.\n\n\"After the storm, the **crew** at the yard **checked** every trailer.\" What happened? Checked. Who checked? The crew. \"At the yard\" and \"after the storm\" are extra details."),
  T("## Compound subjects and verbs\nA sentence can have two subjects or two verbs sharing one job:\n\n- \"**Isaac and his dispatcher** planned the route.\" (two subjects)\n- \"The truck **stopped**, **refueled** and **left**.\" (three verbs)"),
  N("The hidden subject", "Commands have an invisible subject: **you**. \"Send the invoice.\" means \"(You) send the invoice.\" That's a complete sentence."),
  E("Is it a sentence?", "\"Because the shipment arrived late.\"",
    ["Verb: arrived. Subject: the shipment.", "But \"because\" makes the reader wait for the rest: because it arrived late, what happened?", "It isn't a complete thought."], "**Not a sentence.** It's a fragment. Fix: \"Because the shipment arrived late, we lost the customer.\"")
 ],
 "practice": [
  MC("What is the subject? \"Every morning, the owner of the company reviews the numbers.\"", ["Every morning", "The owner", "The company", "The numbers"], 1, "Who reviews? The owner. \"Of the company\" just describes the owner."),
  MC("What is the verb? \"The new drivers from Tampa start on Monday.\"", ["drivers", "Tampa", "start", "Monday"], 2, "What's happening? Starting."),
  MC("Which is a complete sentence?", ["Running late again.", "Call me when you land.", "When the deal closes.", "The broker who called yesterday."], 1, "A command with the hidden subject \"you\"."),
  MC("Which has a compound subject?", ["She signed and sent the contract.", "The lawyer and the buyer met at noon.", "We met at noon and left at one.", "He called twice."], 1, "Two people share the verb \"met\"."),
  MC("\"Although profits were up.\" What's wrong?", ["Nothing", "No verb", "No subject", "It's not a complete thought"], 3, "\"Although\" leaves the reader waiting for the main idea.")
 ]})

L.append({"id": "fragments-and-run-ons", "title": "Fragments and run-ons", "band": "Grade 7", "minutes": 16,
 "lede": "The two most common sentence errors, and the four ways to fix every run-on.",
 "sections": [
  T("## Fragments\nA fragment is a piece of a sentence punctuated as if it were whole. The usual causes:\n\n- **Missing subject or verb:** \"Waiting at the dock for two hours.\" Who was waiting?\n- **A dependent clause standing alone:** \"Because the price dropped.\" \"Which made no sense.\"\n\nFix it by attaching it to the sentence next to it, or by adding what's missing."),
  E("Attach the fragment", "\"We switched suppliers. Because the price dropped.\"",
    ["The second piece starts with \"because\" and can't stand alone.", "Join it to the sentence it explains."], "\"We switched suppliers because the price dropped.\""),
  T("## Run-ons and comma splices\nA **run-on** jams two complete sentences together with nothing between them. A **comma splice** joins them with only a comma.\n\n- Run-on: \"The load is ready it leaves at six.\"\n- Comma splice: \"The load is ready, it leaves at six.\"\n\nBoth are errors because a comma alone can't hold two sentences together."),
  T("## Four fixes\n| Fix | Example |\n|---|---|\n| 1. Period | The load is ready. It leaves at six. |\n| 2. Semicolon | The load is ready; it leaves at six. |\n| 3. Comma + FANBOYS | The load is ready, and it leaves at six. |\n| 4. Make one part depend | Since the load is ready, it leaves at six. |\n\n**FANBOYS** are the seven joining words that can follow a comma: **f**or, **a**nd, **n**or, **b**ut, **o**r, **y**et, **s**o."),
  N("Choosing a fix", "A period gives punch. A semicolon says the two ideas are closely tied. A FANBOYS word names the relationship (but = contrast, so = result). A dependent clause shows which idea matters more.")
 ],
 "practice": [
  MC("Which is a comma splice?", ["I called, she answered.", "I called, and she answered.", "I called; she answered.", "When I called, she answered."], 0, "Two full sentences joined by just a comma."),
  MC("Which fixes \"Rates went up we raised prices\"?", ["Rates went up, we raised prices.", "Rates went up, so we raised prices.", "Rates went up we, raised prices.", "Rates, went up we raised prices."], 1, "Comma plus a FANBOYS word (so)."),
  MC("Which is a fragment?", ["Stop.", "The trucks are fueled.", "Hoping the check clears by Friday.", "She hopes the check clears."], 2, "No subject: who is hoping?"),
  MC("Which joining word can correctly follow a comma to link two sentences?", ["however", "therefore", "yet", "also"], 2, "Yet is a FANBOYS word. \"However\" and \"therefore\" need a semicolon or period before them."),
  MC("\"The deal fell through. Which cost us a month.\" Best fix?", ["The deal fell through, which cost us a month.", "The deal fell through which. Cost us a month.", "The deal fell through; which cost us a month.", "Leave it"], 0, "Attach the \"which\" clause with a comma.")
 ]})

L.append({"id": "punctuation-essentials", "title": "Punctuation essentials", "band": "Grade 7", "minutes": 18,
 "lede": "Apostrophes, colons, semicolons, dashes and quotation marks, with the rules that actually matter.",
 "sections": [
  T("## Apostrophes do two jobs\n1. **Possession:** the driver's truck (one driver), the drivers' trucks (several drivers). For a plural ending in s, put the apostrophe after the s.\n2. **Contractions:** it's = it is, don't = do not, you're = you are.\n\nApostrophes **never** make a plain plural. \"Three truck's\" is wrong; it's \"three trucks.\""),
  N("Its vs it's", "**It's** always means \"it is\" or \"it has.\" **Its** is possessive, like his or her. Test: swap in \"it is.\" \"The company lost **its** best client\" can't become \"lost it is best client,\" so no apostrophe."),
  T("## Colons and semicolons\n- **Colon (:)** introduces something: a list, an explanation, or a punchline. It must come after a complete sentence. \"You need three things: a CDL, insurance and a truck.\"\n- **Semicolon (;)** joins two complete sentences that are closely related. \"The price was fair; we signed.\" It can also separate list items that contain commas."),
  T("## Dashes\nA dash (—) adds emphasis or an interruption. \"We had one problem — the broker never paid.\" Use dashes sparingly; too many make writing feel breathless."),
  T("## Quotation marks (American style)\n- Periods and commas go **inside** the closing quote: He said, \"We're done.\"\n- Question marks go inside only if the quote itself is a question: She asked, \"Is it paid?\" but Did he say \"tomorrow\"?\n- Colons and semicolons go **outside**."),
  E("Fix the punctuation", "\"The companys best month was July its when the produce loads peak.\"",
    ["The company owns the month: company's.", "\"its\" here means \"it is\": it's.", "Two sentences need a break: use a semicolon or a period."], "\"The company's best month was July; it's when the produce loads peak.\"")
 ],
 "practice": [
  MC("Which is correct?", ["The dog wagged it's tail.", "The dog wagged its tail.", "The dog wagged its' tail.", "The dog wagged it is tail."], 1, "Possessive its has no apostrophe."),
  MC("Three brokers share one office. Which is correct?", ["The brokers office", "The broker's office", "The brokers' office", "The brokers's office"], 2, "Plural ending in s: apostrophe after the s."),
  MC("Which uses a colon correctly?", ["We need: fuel, tires and oil.", "We need three things: fuel, tires and oil.", "We: need fuel.", "Because: we're out."], 1, "A colon must follow a complete sentence."),
  MC("Which is punctuated correctly (American style)?", ["He said, \"It's done\".", "He said, \"It's done.\"", "He said \"It's done\".", "He said, 'It's done'."], 1, "The period goes inside the quotes."),
  MC("Which sentence needs a semicolon?", ["We closed the deal and celebrated", "The market dipped we bought more", "After the call we left", "She called twice"], 1, "Two complete sentences jammed together: \"The market dipped; we bought more.\""),
  MC("\"Your/You're going to need a bigger truck.\" Which word fits?", ["Your", "You're"], 1, "You are going to need…")
 ]})

L.append({"id": "commas-without-guessing", "title": "Commas without guessing", "band": "Grade 7", "minutes": 18,
 "lede": "Six rules cover almost every comma you'll ever need. If none applies, leave it out.",
 "sections": [
  T("## The six rules\n1. **Lists of three or more:** fuel, tires, and oil. (The last comma, called the Oxford comma, is optional. Pick one style and stay consistent.)\n2. **Two sentences joined by FANBOYS:** We called, but nobody answered.\n3. **After an introduction:** After the meeting, we signed. / However, the rate changed.\n4. **Around extra information** that could be removed: My truck, which is a 2019 Freightliner, needs tires.\n5. **Direct address:** Isaac, call me back.\n6. **Between equal adjectives:** a long, hot drive. (Test: if you can put \"and\" between them, use a comma.)"),
  T("## Which vs that\n- **That** introduces information you need: \"The truck **that** broke down is in the shop.\" (Which truck? The one that broke down.) No commas.\n- **Which** introduces extra information: \"Our newest truck, **which** cost $160,000, broke down.\" Commas around it.\n\nIf you can delete the clause and the sentence still identifies what you mean, it's extra: use which and commas."),
  N("The big comma mistake", "Never put a single comma between a subject and its verb. \"The man who called this morning, wants a quote\" is wrong. The subject (the man who called this morning) and the verb (wants) stay together."),
  E("Add the commas", "\"Before we left Mike checked the oil the tires and the lights.\"",
    ["\"Before we left\" is an introduction: comma after it.", "The oil, the tires and the lights is a list: commas between items."], "\"Before we left, Mike checked the oil, the tires and the lights.\"")
 ],
 "practice": [
  MC("Which is correct?", ["After we eat we'll talk.", "After we eat, we'll talk.", "After, we eat we'll talk.", "After we eat we'll, talk."], 1, "Comma after an introductory clause."),
  MC("Which is correct?", ["The driver, who was late got fired.", "The driver who was late, got fired.", "The driver who was late got fired.", "The driver, who was late, got, fired."], 2, "\"Who was late\" identifies which driver, so no commas."),
  MC("Which is correct?", ["My brother, who lives in Tampa, is visiting.", "My brother who lives in Tampa, is visiting.", "My brother, who lives in Tampa is visiting.", "My, brother who lives in Tampa is visiting."], 0, "If you have one brother, where he lives is extra information: commas on both sides."),
  MC("Which is correct?", ["I bid on the load but I didn't get it.", "I bid on the load, but I didn't get it.", "I bid on the load but, I didn't get it.", "I bid, on the load but I didn't get it."], 1, "Two full sentences joined by \"but\": comma before it."),
  MC("Which needs a comma?", ["Call me tomorrow.", "Mike call me tomorrow.", "I'll call tomorrow.", "Tomorrow works."], 1, "Direct address: \"Mike, call me tomorrow.\""),
  MC("Which is wrong?", ["The report that you sent was great.", "The report, which you sent Monday, was great.", "The man who called this morning, wants a quote.", "Honestly, it was great."], 2, "Comma between subject and verb.")
 ]})

L.append({"id": "active-voice", "title": "Active voice", "band": "Grade 7", "minutes": 14,
 "lede": "Put the doer first. It's the single easiest way to make writing clearer and stronger.",
 "sections": [
  T("## Active vs passive\n- **Active:** the subject does the action. \"Mike loaded the truck.\"\n- **Passive:** the subject receives the action. \"The truck was loaded by Mike.\"\n\nPassive sentences are longer, weaker, and often hide who did what."),
  T("## How to spot passive voice\nLook for a form of **be** (is, are, was, were, been, being) plus a past-tense verb (loaded, sent, made).\n\nThe zombie test: if you can add \"by zombies\" after the verb and it still makes sense, it's passive. \"Mistakes were made (by zombies).\" Passive."),
  E("Flip it", "\"The payment was not received by our office.\"",
    ["Who did the action? Our office (didn't receive).", "Put the doer first."], "\"Our office didn't receive the payment.\""),
  T("## When passive is fine\nPassive is useful when the doer is unknown or doesn't matter: \"The road was closed for repairs.\" Use it on purpose, not by accident."),
  N("Strong verbs", "Active voice pairs with strong verbs. Replace \"made a decision\" with \"decided,\" \"gave approval\" with \"approved,\" and \"is in need of\" with \"needs.\"")
 ],
 "practice": [
  MC("Which is active?", ["The contract was signed by both parties.", "Both parties signed the contract.", "The contract has been signed.", "Signing was done."], 1, "The doers come first."),
  MC("Which is passive?", ["We missed the deadline.", "The deadline was missed.", "She drove all night.", "They paid on time."], 1, "\"Was missed\" — missed by whom? (By zombies works.)"),
  MC("Best rewrite of \"A decision was made by the board to expand.\"", ["The board decided to expand.", "Expansion was decided by the board.", "It was decided to expand.", "A decision to expand was made."], 0, "Doer first, strong verb."),
  MC("When is passive voice a good choice?", ["Always", "Never", "When the doer is unknown or doesn't matter", "In every email"], 2, "\"My truck was stolen\": you don't know who did it."),
  MC("Replace \"is in need of\" with one strong verb.", ["requires of", "needs", "is needing", "has need"], 1, "Shorter and stronger.")
 ]})

for l in L:
    json.dump(l, open(os.path.join(OUT, l["id"] + ".json"), "w"), ensure_ascii=False, indent=1)
print([l["id"] for l in L])
