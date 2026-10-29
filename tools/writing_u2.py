from common import *
L = []
L.append({"id": "topic-sentences", "title": "Topic sentences", "band": "Grades 7–8", "minutes": 14,
 "lede": "The first sentence of a paragraph should tell the reader exactly what the paragraph will prove.",
 "sections": [
  T("## One paragraph, one point\nA paragraph is a unit of thought: one main idea, supported. The **topic sentence** states that idea, usually first, so the reader knows what's coming."),
  T("## What makes a strong one\n- **Specific:** not \"Trucking is interesting\" but \"Fuel is the biggest cost a small trucking company can control.\"\n- **Arguable or informative:** it makes a claim the rest of the paragraph supports.\n- **Not too broad, not too narrow:** it should fit in one paragraph. \"The history of transportation\" is a book. \"The truck cost $3,200 to fix\" is a detail."),
  E("Strengthen it", "Weak: \"There are many things about customer service.\"",
    ["What's the actual point? Pick one.", "Make it specific and arguable."], "Strong: \"**Answering the phone on the first ring wins more repeat customers than any discount.**\""),
  N("The test", "Cover everything except the topic sentence. Could a reader guess what the paragraph argues? If not, rewrite it.")
 ],
 "practice": [
  MC("Which is the strongest topic sentence?", ["This paragraph is about safety.", "Safety is important.", "Daily pre-trip inspections prevent the most expensive breakdowns.", "There are many safety rules."], 2, "Specific and arguable."),
  MC("Which is too broad for one paragraph?", ["The history of world trade", "Why we switched fuel cards", "How I set my weekly rate", "The best time to call brokers"], 0, "That's a whole book."),
  MC("Where does a topic sentence usually go?", ["Last", "First", "Middle", "Anywhere"], 1, "First, so the reader knows where you're headed."),
  MC("Which is too narrow to be a topic sentence?", ["Late payments hurt small carriers most.", "The invoice was dated March 3.", "Good dispatchers save money.", "Brokers vary in how fast they pay."], 1, "That's a detail, not a main idea.")
 ]})

L.append({"id": "evidence-and-explanation", "title": "Evidence and explanation", "band": "Grades 7–8", "minutes": 16,
 "lede": "Claims need proof, and proof needs explaining. The C-E-R pattern does both.",
 "sections": [
  T("## Claim, Evidence, Reasoning\nA strong paragraph has three parts:\n\n1. **Claim:** what you're saying (the topic sentence).\n2. **Evidence:** facts, numbers, examples or quotes that support it.\n3. **Reasoning:** how the evidence proves the claim. This is the part most people skip."),
  E("C-E-R in action", "Claim: \"Switching to the Pilot fuel card was worth it.\"",
    ["Evidence: \"Our average price dropped from $3.89 to $3.62 a gallon, and we buy about 2,000 gallons a month.\"", "Reasoning: \"That 27-cent discount saves about $540 a month, which covers the card's annual fee in the first week.\""], "Claim → proof → why the proof matters."),
  T("## Good evidence is\n- **Specific:** numbers and names beat \"a lot\" and \"some people.\"\n- **Relevant:** it supports **this** claim, not a nearby one.\n- **Credible:** from a source the reader trusts."),
  N("Don't drop a quote and run", "Never end a paragraph on evidence. After every fact or quote, add at least one sentence explaining what it shows.")
 ],
 "practice": [
  MC("Which part of C-E-R explains HOW the evidence supports the claim?", ["Claim", "Evidence", "Reasoning", "Conclusion"], 2, "Reasoning connects the dots."),
  MC("Which is the best evidence for \"Our new route is faster\"?", ["Drivers like it.", "It's a nicer drive.", "Average trip time dropped from 6.5 to 5.4 hours over 40 trips.", "Everyone says so."], 2, "Specific, measurable, relevant."),
  MC("What's wrong with ending a paragraph on a quote?", ["Nothing", "The reader doesn't know what it proves", "Quotes are illegal", "It's too short"], 1, "Explain what the evidence shows."),
  MC("\"Some people think\" is weak evidence because it's…", ["Too specific", "Vague and unsourced", "Too long", "Too formal"], 1, "Who? How many?")
 ]})

L.append({"id": "transitions", "title": "Transitions", "band": "Grades 7–8", "minutes": 12,
 "lede": "Transition words tell the reader how one idea connects to the next.",
 "sections": [
  T("## Transitions by job\n| Job | Words |\n|---|---|\n| Add | also, in addition, moreover, furthermore |\n| Contrast | however, but, on the other hand, yet |\n| Cause and effect | because, so, therefore, as a result, consequently |\n| Example | for example, for instance, such as |\n| Sequence | first, next, then, finally |\n| Conclude | in short, overall, in the end |"),
  T("## Use the right one\nA transition is a promise. \"However\" promises a contrast; \"therefore\" promises a conclusion. Using the wrong one confuses readers even when every sentence is fine."),
  N("Punctuation with however and therefore", "These aren't joining words like \"but.\" Use a period or semicolon before them: \"Rates rose; **however**, volume held steady.\""),
  E("Fix the connection", "\"Fuel went up 20%. We raised our rates.\"",
    ["The second sentence is a result of the first.", "Add a cause-and-effect transition."], "\"Fuel went up 20%. **As a result**, we raised our rates.\"")
 ],
 "practice": [
  MC("Which transition shows contrast?", ["Furthermore", "However", "Therefore", "For example"], 1, "However = but."),
  MC("\"Sales doubled. ___, we hired two drivers.\"", ["However", "For example", "As a result", "On the other hand"], 2, "Cause and effect."),
  MC("Which is punctuated correctly?", ["Rates rose, however volume held.", "Rates rose; however, volume held.", "Rates rose however, volume held.", "Rates, rose however volume held."], 1, "Semicolon before, comma after."),
  MC("\"Many costs are fixed. ___, insurance and truck payments don't change with miles.\"", ["For example", "However", "Finally", "In contrast"], 0, "It gives examples of fixed costs.")
 ]})

L.append({"id": "concision-cutting-the-fat", "title": "Concision: cutting the fat", "band": "Grade 8", "minutes": 14,
 "lede": "Say it in fewer words. Every word you cut makes the rest hit harder.",
 "sections": [
  T("## Wordy phrases and their replacements\n| Instead of | Write |\n|---|---|\n| in order to | to |\n| due to the fact that | because |\n| at this point in time | now |\n| in the event that | if |\n| has the ability to | can |\n| make a decision | decide |\n| a large number of | many |\n| until such time as | until |"),
  T("## Cut these on sight\n- **Fillers:** just, really, very, actually, basically, kind of.\n- **Throat-clearing:** \"I'm writing to let you know that…\", \"It is important to note that…\"\n- **Doubles:** \"each and every,\" \"first and foremost,\" \"true facts.\""),
  E("Cut by half", "\"I just wanted to reach out to let you know that, due to the fact that our truck is in the shop, we basically won't be able to make the pickup at this point in time.\" (38 words)",
    ["Cut the throat-clearing: \"I just wanted to reach out to let you know that.\"", "due to the fact that → because. at this point in time → today. basically → cut."], "\"Our truck is in the shop, so we can't make today's pickup.\" (**12 words**)"),
  N("The read-aloud rule", "Read your draft out loud. Anything you'd never say in conversation is probably padding.")
 ],
 "practice": [
  MC("Shortest version of \"in the event that\":", ["if", "when the event", "in case of event", "should it be that"], 0, "If."),
  MC("Which is most concise?", ["We made the decision to expand.", "We decided to expand.", "A decision was made by us to expand.", "We came to a decision regarding expansion."], 1, "Verb instead of noun phrase."),
  MC("Which word is filler in \"It's actually a really good deal\"?", ["deal", "good", "actually and really", "It's"], 2, "\"It's a good deal.\""),
  MC("\"Each and every driver\" is better as…", ["Every driver", "Each and all drivers", "The drivers each", "All of every driver"], 0, "Doubles add nothing.")
 ]})
save("writing", L)
