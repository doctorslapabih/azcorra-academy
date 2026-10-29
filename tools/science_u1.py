import json, os
OUT = os.path.join(os.path.dirname(__file__), "..", "data", "lessons", "science")
os.makedirs(OUT, exist_ok=True)
def T(md): return {"type": "text", "md": md}
def N(label, md): return {"type": "note", "label": label, "md": md}
def E(title, problem, steps, answer): return {"type": "example", "title": title, "problem": problem, "steps": steps, "answer": answer}
def MC(q, options, answer, why): return {"type": "mc", "q": q, "options": options, "answer": answer, "why": why}
def NUM(q, answer, why, tol=0.001, unit=None):
    d = {"type": "num", "q": q, "answer": answer, "why": why, "tol": tol}
    if unit: d["unit"] = unit
    return d
NGSS = {"title": "NGSS Science and Engineering Practices (ExploreLearning)", "url": "https://explorelearning.com/resources/insights/ngss-science-and-engineering-practices"}
NIST = {"title": "SI units (NIST)", "url": "https://www.nist.gov/pml/owm/metric-si/si-units"}
L = []

L.append({"id": "the-scientific-method", "title": "The scientific method", "band": "Grade 7", "minutes": 16,
 "lede": "Science is a method for not fooling yourself. Here's how it works, and what hypothesis, theory and law really mean.",
 "sections": [
  T("## A loop, not a recipe\nScientists don't march through fixed steps. They loop:\n\n1. **Observe** and ask a question.\n2. **Research** what's already known.\n3. Form a **hypothesis**: a testable prediction.\n4. **Test** it with an experiment or careful observations.\n5. **Analyze** the data.\n6. **Conclude** and share, which leads to new questions.\n\nA result that disagrees with the hypothesis isn't a failure. It's information."),
  T("## What makes a good hypothesis\nA hypothesis must be **testable** and **falsifiable**: there has to be some result that would prove it wrong.\n\n- Weak: \"Premium diesel is better.\" (Better how? How would you know?)\n- Strong: \"If we switch to premium diesel, the truck's miles per gallon will increase by at least 3% over 2,000 miles.\"\n\nThe if-then format forces you to name what you'll change and what you'll measure."),
  {"type": "terms", "label": "Words scientists use carefully", "terms": [
   {"term": "Hypothesis", "def": "A testable prediction for a specific question."},
   {"term": "Theory", "def": "A well-tested explanation of how something works, supported by large amounts of evidence. Evolution and germ theory are theories. In science, \"theory\" does not mean \"guess.\""},
   {"term": "Law", "def": "A description of what always happens, often as an equation, like Newton's law of gravity. Laws describe; theories explain why."}]},
  T("## The practices scientists actually use\nThe Next Generation Science Standards describe eight practices: asking questions, developing models, planning investigations, analyzing data, using math, constructing explanations, arguing from evidence, and communicating results. Notice how many are about **evidence** and **communication**. Science is a public argument, settled by data."),
  E("Design a quick test", "Question: does a cold call get more answers at 9 a.m. or 2 p.m.?",
    ["Hypothesis: if I call at 9 a.m., more people will answer than at 2 p.m.", "Test: make 50 calls at each time to similar lists.", "Measure: percent answered at each time.", "Conclude: compare the two percents, then repeat with new lists to be sure."], "A real experiment you could run this week.")
 ],
 "practice": [
  MC("Which is a testable hypothesis?", ["Blue is the best color.", "If plants get more light, they will grow taller in 3 weeks.", "Science is interesting.", "Some people like trucks."], 1, "It names a change (light) and a measurement (height)."),
  MC("In science, a theory is…", ["A wild guess", "A well-tested explanation backed by lots of evidence", "Something that hasn't been proven", "The same as a hypothesis"], 1, "Everyday \"theory\" and scientific \"theory\" mean very different things."),
  MC("An experiment's result contradicts your hypothesis. What should you do?", ["Hide the result", "Change the data", "Accept it, revise the hypothesis and test again", "Stop doing science"], 2, "Disproved hypotheses move science forward."),
  MC("What does \"falsifiable\" mean?", ["It's false", "Some possible result could prove it wrong", "It's been proven", "It's a lie"], 1, "If nothing could ever disprove it, it isn't scientific."),
  MC("Laws vs theories: which is true?", ["Theories become laws when proven", "Laws describe what happens; theories explain why", "Laws are guesses", "They're the same"], 1, "They're different kinds of knowledge. A theory never \"graduates\" into a law.")
 ],
 "sources": [NGSS]})

L.append({"id": "variables-and-controls", "title": "Variables and controls", "band": "Grade 7", "minutes": 18,
 "lede": "How to run a fair test, and why correlation isn't causation.",
 "sections": [
  T("## Three kinds of variable\n| Variable | What it is | Example (testing tire pressure vs fuel economy) |\n|---|---|---|\n| Independent | What **you** change | Tire pressure |\n| Dependent | What you **measure** | Miles per gallon |\n| Controlled | What you keep the **same** | Truck, load weight, route, speed, driver |\n\nChange one thing at a time. If you change the pressure **and** the route, you can't tell which one moved the mpg."),
  T("## Control groups\nA **control group** gets no treatment, so you have something to compare against. To test a new fuel additive, run some trucks with it and some without, on the same routes.\n\nIn medicine, the control group often gets a **placebo**: a fake treatment that looks real. In a **double-blind** study, neither the patients nor the researchers know who got what, so expectations can't bend the results."),
  T("## Sample size\nOne trip proves nothing. Traffic, weather and luck add noise. More trials and bigger samples make results more trustworthy, because random noise averages out."),
  T("## Correlation is not causation\nTwo things can rise together without one causing the other. Ice cream sales and drownings both rise in summer. Ice cream doesn't cause drowning; **hot weather** drives both. That hidden driver is called a **confounding variable**.\n\nThe only reliable way to show cause is an experiment where you change one thing and control the rest."),
  E("Spot the flaw", "A shop says: \"Customers who bought our premium oil had 30% fewer breakdowns.\"",
    ["Who buys premium oil? Probably owners who maintain trucks carefully in general.", "Careful maintenance could be the real cause.", "There's no control group of careful owners using regular oil."], "**Correlation, not proven causation.** A confounding variable (careful owners) could explain it.")
 ],
 "practice": [
  MC("You test whether music affects typing speed. The independent variable is…", ["Typing speed", "Music", "The keyboard", "The person"], 1, "It's what you change."),
  MC("In the same test, the dependent variable is…", ["Music", "Typing speed", "Room temperature", "Time of day"], 1, "It's what you measure."),
  MC("Why use a control group?", ["To save money", "To have a baseline to compare against", "To make results bigger", "It's not needed"], 1, "Without it, you can't tell if the treatment did anything."),
  MC("Cities with more firefighters have more fire damage. Most likely explanation?", ["Firefighters cause damage", "Bigger cities have more fires and more firefighters", "It's random", "Damage causes firefighters"], 1, "City size is the confounding variable."),
  MC("In a double-blind study…", ["Only patients don't know who got the real treatment", "Neither patients nor researchers know", "Everyone knows", "There's no placebo"], 1, "It keeps expectations from skewing results."),
  MC("Which is the most trustworthy test of a new tire?", ["One truck, one trip", "20 trucks with new tires and 20 with old, same routes, 3 months", "Asking drivers how it feels", "Reading the ad"], 1, "Big sample, control group, same conditions.")
 ],
 "sources": [NGSS]})

L.append({"id": "measurement-and-units", "title": "Measurement and units", "band": "Grade 7", "minutes": 18,
 "lede": "The metric system, the prefixes that make it easy, and the difference between accurate and precise.",
 "sections": [
  T("## The SI system\nScience worldwide uses the **International System of Units (SI)**, the modern metric system. Seven base units define everything else:\n\n| Quantity | Unit | Symbol |\n|---|---|---|\n| Length | meter | m |\n| Mass | kilogram | kg |\n| Time | second | s |\n| Temperature | kelvin | K |\n| Electric current | ampere | A |\n| Amount of substance | mole | mol |\n| Light intensity | candela | cd |"),
  T("## Prefixes do the heavy lifting\nEvery metric unit scales by powers of 10, using the same prefixes:\n\n| Prefix | Symbol | Means |\n|---|---|---|\n| mega | M | 1,000,000 |\n| kilo | k | 1,000 |\n| centi | c | 1/100 |\n| milli | m | 1/1,000 |\n| micro | μ | 1/1,000,000 |\n\nSo 1 kilometer = 1,000 meters, 1 milligram = 1/1,000 of a gram. To convert, just move the decimal."),
  E("Metric conversion", "Convert 2.4 kilometers to meters, then to centimeters.",
    ["1 km = 1,000 m, so 2.4 km = 2,400 m.", "1 m = 100 cm, so 2,400 m = 240,000 cm."], "**2,400 m = 240,000 cm**"),
  T("## Accuracy vs precision\n- **Accurate:** close to the true value.\n- **Precise:** repeated measurements are close to each other.\n\nA scale that always reads 2 lb heavy is precise but not accurate. Good measurement needs both. That's why trucks get weighed on certified scales."),
  N("Useful conversions", "1 inch = 2.54 cm (exactly). 1 mile ≈ 1.609 km. 1 kg ≈ 2.205 lb. 1 gallon ≈ 3.785 liters."),
  E("Imperial to metric", "A loaded truck weighs 80,000 lb. About how many kilograms?",
    ["1 kg ≈ 2.205 lb, so divide.", "80,000 ÷ 2.205 ≈ 36,281."], "**About 36,300 kg** (about 36 metric tons)")
 ],
 "practice": [
  NUM("How many meters are in 3.5 km?", 3500, "1 km = 1,000 m.", unit="m"),
  NUM("How many grams are in 750 mg?", 0.75, "750 ÷ 1,000.", unit="g"),
  MC("What is the SI base unit of mass?", ["Gram", "Pound", "Kilogram", "Newton"], 2, "The kilogram is the base unit, even though it has a prefix."),
  MC("A dart player's darts all land tightly together but far from the bullseye. They are…", ["Accurate and precise", "Precise but not accurate", "Accurate but not precise", "Neither"], 1, "Close to each other, far from the target."),
  NUM("How many centimeters are in 6 inches? (1 in = 2.54 cm)", 15.24, "6 × 2.54.", unit="cm"),
  NUM("About how many liters is a 150-gallon fuel tank? Round to the nearest whole number. (1 gal ≈ 3.785 L)", 568, "150 × 3.785 = 567.75.", tol=1, unit="L")
 ],
 "sources": [NIST]})

L.append({"id": "reading-graphs-and-data", "title": "Reading graphs and data", "band": "Grade 7", "minutes": 18,
 "lede": "How to read a graph in ten seconds, find the rate in a slope, and catch a misleading chart.",
 "sections": [
  T("## Pick the right graph\n| Graph | Best for | Example |\n|---|---|---|\n| Line | Change over time | Fuel price by month |\n| Bar | Comparing categories | Revenue per customer |\n| Scatter | Relationship between two numbers | Speed vs mpg for 50 trips |\n| Pie | Parts of a whole (few parts) | Share of costs |"),
  T("## Read any graph in four steps\n1. **Title:** what is this about?\n2. **Axes:** what's on each, and in what **units**?\n3. **Scale:** what does each gridline count by? Does the axis start at zero?\n4. **Shape:** rising, falling, flat, curved? Any outliers?"),
  T("## Slope is a rate\nOn a line graph, steepness shows how fast something changes. Slope = rise ÷ run = change in y ÷ change in x.\n\nIf a distance-time graph rises 120 miles over 2 hours, the slope is 60 miles per hour: the speed."),
  E("Find the rate", "A graph shows a fuel tank at 150 gallons at 6 a.m. and 90 gallons at 10 a.m.",
    ["Change in fuel: 90 − 150 = −60 gallons.", "Change in time: 4 hours.", "Slope: −60 ÷ 4 = −15."], "**−15 gallons per hour** (burning 15 gallons an hour)"),
  T("## Catching misleading graphs\n- **Truncated axis:** a y-axis that starts at 95 instead of 0 makes a 2% difference look huge.\n- **Missing units or labels:** you can't interpret it.\n- **Cherry-picked time window:** showing only the months that fit the story.\n- **Area tricks:** pictures scaled in two directions exaggerate differences.\n\nWhen a chart looks dramatic, check the axis first."),
  N("Outliers", "An outlier is a point far from the rest, like one trip with 2 mpg because of a mountain climb in a storm. Investigate outliers before deleting them; sometimes they're the most interesting data.")
 ],
 "practice": [
  MC("Best graph for monthly revenue over two years?", ["Pie", "Line", "Scatter", "None"], 1, "Change over time."),
  MC("Best graph to see if heavier loads lower mpg across 80 trips?", ["Pie", "Bar", "Scatter", "Line"], 2, "Relationship between two numbers."),
  NUM("A line rises from 20 miles at 1 hour to 200 miles at 4 hours. What's the slope?", 60, "(200 − 20) ÷ (4 − 1) = 180 ÷ 3.", unit="mph"),
  MC("A bar chart's y-axis starts at 98. The bars read 99 and 100. What's the issue?", ["None", "The truncated axis exaggerates a small difference", "Too many bars", "Wrong colors"], 1, "From zero, those bars would look almost identical."),
  MC("What should you check first on any graph?", ["Colors", "Axes and units", "The font", "The legend color"], 1, "Without units, the numbers mean nothing."),
  NUM("A tank goes from 150 to 90 gallons between 6 and 10 a.m. What's the rate in gallons per hour (use a negative for decreasing)?", -15, "−60 ÷ 4.")
 ],
 "sources": [NGSS]})

for l in L:
    json.dump(l, open(os.path.join(OUT, l["id"] + ".json"), "w"), ensure_ascii=False, indent=1)
print([l["id"] for l in L])
