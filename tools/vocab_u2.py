from common import *
def wordtable(rows):
    return T("| Word | Meaning | In a sentence |\n|---|---|---|\n" + "\n".join(f"| **{w}** | {m} | {s} |" for w, m, s in rows))
L = []
L.append({"id": "words-for-thinking-analyze-infer-evaluate", "title": "Words for thinking: analyze, infer, evaluate", "band": "Grades 7–8", "minutes": 14,
 "lede": "The verbs teachers, tests and bosses use when they want you to think, not just remember.",
 "sections": [
  T("## Why these matter\nQuestions use these words to tell you exactly what kind of thinking they want. \"Describe\" and \"evaluate\" ask for completely different answers. Misread the verb and you answer the wrong question."),
  wordtable([
   ("analyze", "break into parts to see how it works", "Analyze last month's costs by category."),
   ("infer", "conclude from evidence that isn't stated directly", "From his silence, I inferred he wasn't interested."),
   ("evaluate", "judge the value or quality of", "Evaluate both offers before you sign."),
   ("synthesize", "combine ideas into something new", "She synthesized three reports into one plan."),
   ("interpret", "explain the meaning of", "How do you interpret this clause?"),
   ("justify", "give reasons that support", "Justify the price increase with numbers."),
   ("distinguish", "show the difference between", "Distinguish fixed costs from variable costs."),
   ("hypothesize", "propose a possible explanation to test", "We hypothesized that the late loads were a routing issue.")]),
  N("Infer vs imply", "The speaker **implies** (hints). The listener **infers** (figures it out). \"He implied the deal was dead; I inferred we should move on.\""),
  E("Match the verb to the task", "\"Evaluate the new dispatch software.\"",
    ["Describing its features isn't enough.", "Evaluate means judge: Is it worth it? What are its strengths and weaknesses? What's your verdict?"], "Give a **judgment with reasons**.")
 ],
 "practice": [
  MC("\"Analyze\" asks you to…", ["Summarize briefly", "Break something into parts to understand it", "Memorize it", "Agree with it"], 1, "Analysis = taking apart."),
  MC("A text says, \"She checked her watch for the fifth time.\" You conclude she's impatient. You…", ["implied", "inferred", "evaluated", "synthesized"], 1, "You drew a conclusion from evidence."),
  MC("\"Justify your answer\" means…", ["Give reasons that support it", "Make it longer", "Check the spelling", "Say it louder"], 0, "Back it up."),
  MC("Combining three articles into one new argument is…", ["Analyzing", "Synthesizing", "Inferring", "Distinguishing"], 1, "Synthesis creates something new from parts."),
  MC("Fill in: \"His tone ___ that he wasn't happy, though he never said so.\"", ["inferred", "implied", "evaluated", "analyzed"], 1, "The speaker implies.")
 ]})

L.append({"id": "words-for-change-and-cause", "title": "Words for change and cause", "band": "Grades 7–8", "minutes": 14,
 "lede": "Precise words for how things change and why they happen.",
 "sections": [
  wordtable([
   ("fluctuate", "rise and fall irregularly", "Fuel prices fluctuate every week."),
   ("escalate", "increase quickly or get more intense", "The argument escalated into a lawsuit."),
   ("diminish", "become smaller or weaker", "Profits diminished after the rate cut."),
   ("transform", "change completely", "Automation transformed the warehouse."),
   ("catalyst", "something that causes change", "The new contract was a catalyst for growth."),
   ("consequence", "a result, often of an action", "Late payments have consequences."),
   ("precipitate", "cause something to happen suddenly", "The storm precipitated a wave of cancellations."),
   ("mitigate", "make less severe", "Insurance mitigates the risk of a wreck."),
   ("exacerbate", "make worse", "Skipping maintenance exacerbated the problem."),
   ("stagnate", "stop developing or moving", "Sales stagnated over the summer.")]),
  N("Mitigate vs exacerbate", "These are opposites, and both are high-value words. You **mitigate** a risk (reduce it) and **exacerbate** a problem (worsen it)."),
  E("Choosing the precise word", "\"Prices went up and down all month.\"",
    ["\"Went up and down\" is vague.", "The single word for irregular rising and falling is fluctuate."], "\"Prices **fluctuated** all month.\"")
 ],
 "practice": [
  MC("A word for \"make less severe\":", ["exacerbate", "mitigate", "escalate", "precipitate"], 1, "Mitigate a risk."),
  MC("\"The new manager was the ___ for a total turnaround.\"", ["consequence", "catalyst", "stagnation", "fluctuation"], 1, "A catalyst causes change."),
  MC("If tension escalates, it…", ["Disappears", "Increases", "Stays the same", "Goes up and down"], 1, "Escalate = intensify."),
  MC("The opposite of \"mitigate\" is…", ["exacerbate", "diminish", "transform", "fluctuate"], 0, "Make worse."),
  MC("\"Revenue ___ for three years: no growth, no decline.\"", ["escalated", "fluctuated", "stagnated", "precipitated"], 2, "Stagnate = stop moving.")
 ]})

L.append({"id": "words-for-amount-and-degree", "title": "Words for amount and degree", "band": "Grades 7–8", "minutes": 14,
 "lede": "Ditch \"a lot,\" \"very\" and \"kind of.\" These words say exactly how much.",
 "sections": [
  wordtable([
   ("abundant", "more than enough", "Work is abundant in peak season."),
   ("scarce", "in short supply", "Drivers were scarce during the shortage."),
   ("negligible", "so small it doesn't matter", "The price difference is negligible."),
   ("substantial", "large in size or importance", "A substantial raise."),
   ("marginal", "small, at the edge", "A marginal improvement."),
   ("excessive", "more than is reasonable", "Excessive idling wastes fuel."),
   ("adequate", "enough, but no more", "The pay was adequate."),
   ("comprehensive", "including everything", "A comprehensive inspection."),
   ("meager", "too small or too little", "A meager profit."),
   ("exponential", "growing faster and faster, by multiplying", "Exponential growth in orders.")]),
  N("Exponential is a math word", "People often use \"exponential\" to mean \"big.\" Strictly, it means growth by repeated multiplication, like doubling every month. Use it when that's what you mean."),
  E("Upgrade the sentence", "\"The fee is really small, so it kind of doesn't matter.\"",
    ["Replace the vague words with one precise one."], "\"The fee is **negligible**.\"")
 ],
 "practice": [
  MC("\"Negligible\" means…", ["Huge", "So small it doesn't matter", "Illegal", "Ignored on purpose"], 1, "Small enough to neglect."),
  MC("The opposite of \"scarce\":", ["meager", "abundant", "marginal", "adequate"], 1, "More than enough."),
  MC("\"The pay was ___\" means it was enough but nothing special.", ["excessive", "adequate", "substantial", "exponential"], 1, "Adequate = just enough."),
  MC("A \"comprehensive\" plan…", ["Covers everything", "Is easy to understand", "Is cheap", "Is short"], 0, "Comprehensive = complete."),
  MC("Which describes growth that doubles every month?", ["Marginal", "Exponential", "Adequate", "Negligible"], 1, "Repeated multiplication.")
 ]})

L.append({"id": "words-for-people-and-character", "title": "Words for people and character", "band": "Grades 7–8", "minutes": 14,
 "lede": "Describe people precisely: in reviews, hiring, stories and deals.",
 "sections": [
  wordtable([
   ("diligent", "hardworking and careful", "A diligent dispatcher catches every error."),
   ("candid", "honest and direct", "Give me your candid opinion."),
   ("tenacious", "refusing to give up", "A tenacious negotiator."),
   ("arrogant", "acting superior to others", "His arrogant tone lost the client."),
   ("humble", "modest about your own importance", "Humble in victory."),
   ("resilient", "recovers quickly from setbacks", "Resilient after a bad quarter."),
   ("pragmatic", "practical, focused on what works", "A pragmatic decision."),
   ("cynical", "believing people act only from self-interest", "Years of bad brokers made him cynical."),
   ("gregarious", "sociable, enjoys company", "A gregarious salesperson."),
   ("meticulous", "extremely careful about details", "Meticulous records.")]),
  N("Connotation", "Words can mean nearly the same thing but feel different. **Tenacious** (positive) vs **stubborn** (negative). **Frugal** (positive) vs **cheap** (negative). Choose the one that matches your judgment."),
  E("Pick the connotation", "Your partner never stops pushing for a better rate. You admire it.",
    ["Stubborn and obstinate sound negative.", "Tenacious and persistent sound positive."], "\"She's **tenacious**.\"")
 ],
 "practice": [
  MC("Someone who bounces back fast after failure is…", ["cynical", "resilient", "arrogant", "candid"], 1, "Resilient = recovers."),
  MC("\"Gregarious\" means…", ["Greedy", "Sociable", "Shy", "Angry"], 1, "Loves company."),
  MC("Which has a positive connotation?", ["stubborn", "cheap", "tenacious", "nosy"], 2, "Tenacious praises persistence."),
  MC("A person who's extremely careful with details is…", ["meticulous", "pragmatic", "humble", "gregarious"], 0, "Meticulous."),
  MC("\"After being burned by three partners, he became ___ about every offer.\"", ["candid", "cynical", "diligent", "humble"], 1, "Expecting self-interest.")
 ]})
save("vocab", L)
