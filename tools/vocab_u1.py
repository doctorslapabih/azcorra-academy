import json, os
OUT = os.path.join(os.path.dirname(__file__), "..", "data", "lessons", "vocab")
os.makedirs(OUT, exist_ok=True)
def T(md): return {"type": "text", "md": md}
def N(label, md): return {"type": "note", "label": label, "md": md}
def E(title, problem, steps, answer): return {"type": "example", "title": title, "problem": problem, "steps": steps, "answer": answer}
def MC(q, options, answer, why): return {"type": "mc", "q": q, "options": options, "answer": answer, "why": why}
L = []

L.append({"id": "context-clues", "title": "Context clues", "band": "Grade 7", "minutes": 15,
 "lede": "Most new words come with hints sitting right next to them. Here's how to read the hints.",
 "sections": [
  T("## Why context comes first\nYou'll meet far more words in reading than anyone can teach you one at a time. The skill that scales is figuring out a word from the sentence around it. Five kinds of clue show up again and again."),
  T("## The five clue types\n| Clue | Signal words | Example |\n|---|---|---|\n| Definition | is, means, refers to, commas or dashes | A **broker**, someone who arranges deals between others, set up the load. |\n| Synonym | or, also, like, in other words | The plan was **feasible**, or doable, with the budget we had. |\n| Antonym or contrast | but, however, unlike, instead | Unlike his **gregarious** brother, Sam kept to himself. |\n| Example | such as, including, for instance | **Perishable** freight, such as produce and dairy, needs a reefer. |\n| General sense | the whole situation | After three missed payments, the lender **repossessed** the truck. |"),
  E("Using a contrast clue", "\"The first offer was **paltry**, but the second was generous enough to accept.\"",
    ["Spot the signal: **but** means the next idea contrasts.", "The second offer was generous.", "So the first was the opposite: small, not enough."], "**Paltry** means small or worthless."),
  T("## The method\n1. Stop at the word. Don't skip it.\n2. Find the signal word, if there is one.\n3. Guess a simple replacement word.\n4. Plug your guess into the sentence. If it reads naturally, you're close.\n5. Check a dictionary later if the word matters."),
  N("Context has limits", "Sometimes the sentence gives no real clue. When the word matters (a contract, a test question), look it up. Context gets you the gist; a dictionary gets you the exact meaning.")
 ],
 "practice": [
  MC("\"The mechanic gave a **cursory** look at the engine, glancing at it for only a few seconds.\" Cursory means…", ["Detailed", "Quick and shallow", "Angry", "Expensive"], 1, "\"Only a few seconds\" is a definition clue."),
  MC("\"Unlike the **frugal** owner, his partner spent money on everything.\" Frugal means…", ["Careful with money", "Wealthy", "Generous", "Lazy"], 0, "\"Unlike\" signals contrast with spending on everything."),
  MC("\"**Arid** regions, such as deserts and dry plains, get little rain.\" Arid means…", ["Cold", "Very dry", "Crowded", "Flat"], 1, "Example clue: deserts and dry plains."),
  MC("\"The new rule was **ambiguous**; even the managers couldn't agree on what it meant.\" Ambiguous means…", ["Unclear", "Strict", "Popular", "Temporary"], 0, "General sense: nobody agreed on the meaning."),
  MC("\"She was **adamant**, refusing to change her mind no matter what we said.\" Adamant means…", ["Unsure", "Firm and unwilling to change", "Polite", "Tired"], 1, "Definition clue right after the comma."),
  MC("\"The tiny cafe was **unassuming**, but the food was the best in the city.\" Unassuming means…", ["Fancy", "Modest, not showy", "Dirty", "Famous"], 1, "\"But\" contrasts a plain place with excellent food.")
 ]})

L.append({"id": "prefixes-that-flip-meaning", "title": "Prefixes that flip meaning", "band": "Grade 7", "minutes": 15,
 "lede": "A prefix is a few letters at the front that change a word's meaning. Twenty of them cover most of what you'll see.",
 "sections": [
  T("## Negative prefixes\nThese flip a word to its opposite or remove something.\n\n| Prefix | Meaning | Examples |\n|---|---|---|\n| un- | not | unfair, unlikely, unsigned |\n| in-, im-, il-, ir- | not | inactive, impossible, illegal, irregular |\n| dis- | not, opposite of | dishonest, disagree, disconnect |\n| non- | not | nonstop, nonprofit, nonnegotiable |\n| mis- | wrongly | misread, mislabel, miscalculate |\n| anti- | against | antivirus, antisocial |\n| counter- | against, opposite | counteroffer, counterproductive |"),
  N("in-, im-, il-, ir- are one prefix", "They're the same \"not\" prefix, changed to match the next sound: **im**- before b, m, p (impossible); **il**- before l (illegal); **ir**- before r (irregular); **in**- everywhere else."),
  T("## Position and time prefixes\n| Prefix | Meaning | Examples |\n|---|---|---|\n| pre- | before | preview, prepay, precaution |\n| post- | after | postpone, postwar |\n| re- | again, back | rebuild, refund, reroute |\n| sub- | under, below | subway, subcontract, subtotal |\n| super- | above, beyond | supervisor, superhuman |\n| inter- | between | interstate, interact |\n| trans- | across | transport, transfer, transatlantic |\n| ex- | out, former | export, ex-partner |\n| co-, com-, con- | together | cooperate, combine, connect |"),
  E("Decoding with a prefix", "What's a **subcontractor**?",
    ["sub- = under.", "contractor = someone hired to do a job.", "Put together: someone hired under another contractor."], "A worker hired **by** the main contractor to do part of the job."),
  N("Not every start is a prefix", "\"Uncle\" doesn't mean not-cle, and \"interest\" isn't between-est. Check that what's left is a real word or root.")
 ],
 "practice": [
  MC("\"Illegible\" handwriting is…", ["Beautiful", "Impossible to read", "Written in pencil", "Illegal"], 1, "il- (not) + legible (readable)."),
  MC("A \"counteroffer\" is…", ["An offer made in response, against the first", "A store discount", "A final offer", "A fake offer"], 0, "counter- = against."),
  MC("To \"misconstrue\" something is to…", ["Build it", "Understand it wrongly", "Repeat it", "Agree with it"], 1, "mis- = wrongly; construe = interpret."),
  MC("\"Interstate\" highways run…", ["Inside one state", "Between states", "Under states", "Around cities"], 1, "inter- = between."),
  MC("Which word means \"to pay before\"?", ["Repay", "Prepay", "Postpay", "Overpay"], 1, "pre- = before."),
  MC("Which prefix correctly makes \"responsible\" negative?", ["un-", "dis-", "ir-", "non-"], 2, "Before r, the \"not\" prefix becomes ir-: irresponsible.")
 ]})

L.append({"id": "suffixes-and-parts-of-speech", "title": "Suffixes and parts of speech", "band": "Grade 7", "minutes": 15,
 "lede": "The ending of a word usually tells you what job it does in a sentence.",
 "sections": [
  T("## Why endings matter\nOne root can become a noun, a verb, an adjective and an adverb just by changing the ending: **profit, profitable, profitably, profiteer**. If you know the root and recognize the ending, you know the word."),
  T("## Noun endings (things, people, ideas)\n| Suffix | Meaning | Examples |\n|---|---|---|\n| -tion, -sion | act or state of | negotiation, decision |\n| -ment | result or act of | payment, agreement |\n| -ness | state of being | awareness, darkness |\n| -ity, -ty | quality of | reliability, loyalty |\n| -er, -or, -ist | person who | driver, investor, analyst |\n| -ance, -ence | state of | compliance, persistence |"),
  T("## Adjective endings (describing words)\n| Suffix | Meaning | Examples |\n|---|---|---|\n| -able, -ible | can be | profitable, flexible |\n| -ful | full of | careful, successful |\n| -less | without | reckless, fearless |\n| -ous, -ious | having | dangerous, ambitious |\n| -ive | tending to | aggressive, productive |\n| -al, -ic | relating to | financial, strategic |"),
  T("## Verb and adverb endings\n| Suffix | Meaning | Examples |\n|---|---|---|\n| -ize, -ise | to make | finalize, prioritize |\n| -ify | to make | simplify, verify |\n| -en | to make | strengthen, widen |\n| -ate | to do or cause | negotiate, activate |\n| -ly (adverb) | in a way that is | quickly, carefully |"),
  E("Building a word family", "Root: **rely**",
    ["Adjective: reli**able** (can be relied on).", "Noun: reli**ability** (the quality of being reliable).", "Adverb: reli**ably**.", "Opposite: **un**reliable."], "One root, four useful words.")
 ],
 "practice": [
  MC("\"Diligence\" is a…", ["Verb", "Noun", "Adjective", "Adverb"], 1, "-ence makes a state or quality: a noun."),
  MC("Which word means \"to make simple\"?", ["Simplicity", "Simply", "Simplify", "Simplest"], 2, "-ify = to make."),
  MC("A \"meticulous\" person is ___. Which part of speech is meticulous?", ["Noun", "Verb", "Adjective", "Adverb"], 2, "-ous is an adjective ending."),
  MC("Which is the adverb?", ["Decisive", "Decision", "Decisively", "Decide"], 2, "-ly turns an adjective into an adverb."),
  MC("\"Feasible\" most likely means…", ["Can be done", "Full of fear", "Without food", "Very large"], 0, "-ible = can be. Feasible = able to be done."),
  MC("Fill the blank: \"We need to ___ the loads by delivery time.\"", ["prioritize", "priority", "prior", "prioritization"], 0, "The sentence needs a verb; -ize makes one.")
 ]})

L.append({"id": "latin-roots-i", "title": "Latin roots I", "band": "Grade 7", "minutes": 18,
 "lede": "Well over half of English words trace back to Latin, many of them through French. These twelve roots unlock hundreds of words.",
 "sections": [
  T("## Twelve high-value Latin roots\n| Root | Meaning | Words |\n|---|---|---|\n| dict | say | predict, contradict, verdict, dictate |\n| port | carry | transport, export, portable, report |\n| rupt | break | bankrupt, interrupt, disrupt, erupt |\n| scrib, script | write | describe, subscription, manuscript |\n| spect | look | inspect, prospect, spectator, respect |\n| struct | build | construct, structure, instruct, obstruct |\n| tract | pull, drag | contract, attract, tractor, extract |\n| vid, vis | see | video, evident, vision, revise |\n| ject | throw | reject, project, inject, eject |\n| mit, miss | send | transmit, permit, mission, dismiss |\n| duc, duct | lead | conduct, produce, deduct, educate |\n| cred | believe | credit, credible, incredible, credentials |"),
  E("Decoding a business word", "What does **bankrupt** literally mean?",
    ["It comes from the Italian banca rotta: banca = bench (a money-changer's table), rotta = broken, from the Latin rupt.", "The traditional story is that a money-changer who couldn't pay his debts had his bench broken."], "**Broken bench**: unable to pay debts."),
  E("Stacking a prefix and a root", "**Transport**",
    ["trans- = across.", "port = carry."], "**To carry across**: moving freight from one place to another."),
  N("Practice move", "When you hit a long word, cover the prefix and suffix and look for a root you know. \"Unpredictable\" = un + pre + dict + able: not able to be said beforehand.")
 ],
 "practice": [
  MC("\"Credible\" evidence is…", ["Believable", "Expensive", "Written down", "Hidden"], 0, "cred = believe; -ible = can be."),
  MC("To \"obstruct\" traffic is to…", ["Speed it up", "Build something in its way", "Count it", "Look at it"], 1, "ob (against) + struct (build)."),
  MC("A \"retrospect\" is a…", ["Look back", "Plan ahead", "Written note", "Broken promise"], 0, "retro (back) + spect (look)."),
  MC("Which root means \"send\"?", ["ject", "mit", "duc", "port"], 1, "Transmit, permit, mission."),
  MC("To \"deduct\" money is to…", ["Add it", "Lead it away, subtract it", "Throw it", "Write it"], 1, "de (away) + duct (lead)."),
  MC("What does \"interrupt\" literally mean?", ["To carry between", "To break between", "To write between", "To look between"], 1, "inter (between) + rupt (break)."),
  MC("A contract \"draws\" two parties together. Which root shows that?", ["tract", "struct", "dict", "spect"], 0, "tract = pull or draw.")
 ]})

L.append({"id": "greek-roots-i", "title": "Greek roots I", "band": "Grade 7", "minutes": 15,
 "lede": "Greek roots run science, medicine and technology. Learn these and technical words stop being scary.",
 "sections": [
  T("## Fifteen Greek roots\n| Root | Meaning | Words |\n|---|---|---|\n| bio | life | biology, biography, antibiotic |\n| graph, gram | write, draw | autograph, telegram, graphic |\n| logy, log | study of, word | geology, psychology, dialogue |\n| phon | sound | telephone, symphony, phonics |\n| photo | light | photograph, photosynthesis |\n| tele | far | telescope, television, telecom |\n| auto | self | automatic, autonomy, autopilot |\n| micro | small | microscope, microchip |\n| macro | large | macroeconomics |\n| chron | time | chronic, chronological, synchronize |\n| geo | earth | geography, geology, geometry |\n| hydro | water | hydrate, hydraulic, hydroelectric |\n| psych | mind | psychology, psychic |\n| therm | heat | thermometer, thermal |\n| meter | measure | odometer, perimeter, speedometer |"),
  E("Decoding a science word", "**Hydrology**",
    ["hydro = water.", "logy = study of."], "**The study of water**."),
  E("Decoding a business word", "**Macroeconomics**",
    ["macro = large.", "economics = how money and resources move."], "**Big-picture economics**: whole countries and markets, as opposed to microeconomics, which looks at single businesses."),
  N("Greek vs Latin", "Latin roots dominate everyday and legal English. Greek roots dominate science, medicine and tech. Many sciences pair them: \"tele-vision\" is Greek tele + Latin vis.")
 ],
 "practice": [
  MC("\"Chronological\" order means…", ["By size", "By time", "By importance", "By color"], 1, "chron = time."),
  MC("A \"thermostat\" controls…", ["Light", "Sound", "Heat", "Water"], 2, "therm = heat."),
  MC("\"Autonomy\" means…", ["Self-rule, independence", "Automatic payment", "A car part", "Group decision"], 0, "auto = self; nomos = law."),
  MC("A \"biography\" is…", ["A study of plants", "A written account of someone's life", "A life insurance plan", "A science lab"], 1, "bio (life) + graph (write)."),
  MC("What does an odometer measure?", ["Speed", "Fuel", "Distance traveled", "Smell"], 2, "Greek hodos (way, road) + meter (measure)."),
  MC("\"Geothermal\" energy comes from…", ["The sun", "Heat inside the earth", "Wind", "Water"], 1, "geo (earth) + therm (heat).")
 ]})

for l in L:
    json.dump(l, open(os.path.join(OUT, l["id"] + ".json"), "w"), ensure_ascii=False, indent=1)
print([l["id"] for l in L])
