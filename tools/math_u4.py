from common import *

STATS = {"title": "OpenStax, Introductory Statistics 2e", "url": "https://openstax.org/details/books/introductory-statistics-2e"}
CMATH = {"title": "OpenStax, Contemporary Mathematics (Probability; Statistics)", "url": "https://openstax.org/details/books/contemporary-mathematics"}

def FIG(svg, caption): return {"type": "figure", "svg": svg, "caption": caption}

BOX_SVG = """<svg viewBox="0 0 560 150" role="img" aria-label="Box plot: minimum 3, first quartile 6, median 8.5, third quartile 12, maximum 15" style="width:100%;max-width:560px;color:var(--ink)">
<line x1="40" y1="110" x2="520" y2="110" stroke="currentColor" stroke-opacity=".35"/>
<g font-size="12" fill="currentColor" text-anchor="middle">
<text x="40" y="128">0</text><text x="136" y="128">4</text><text x="232" y="128">8</text><text x="328" y="128">12</text><text x="424" y="128">16</text><text x="520" y="128">20</text></g>
<line x1="112" y1="60" x2="184" y2="60" stroke="currentColor" stroke-width="2"/>
<line x1="328" y1="60" x2="400" y2="60" stroke="currentColor" stroke-width="2"/>
<line x1="112" y1="45" x2="112" y2="75" stroke="currentColor" stroke-width="2"/>
<line x1="400" y1="45" x2="400" y2="75" stroke="currentColor" stroke-width="2"/>
<rect x="184" y="35" width="144" height="50" fill="var(--sunk)" stroke="currentColor" stroke-width="2"/>
<line x1="244" y1="35" x2="244" y2="85" stroke="var(--accent)" stroke-width="3"/>
<g font-size="12" fill="currentColor" text-anchor="middle">
<text x="112" y="28">min 3</text><text x="184" y="28">Q1 6</text><text x="244" y="22">median 8.5</text><text x="328" y="28">Q3 12</text><text x="400" y="28">max 15</text></g>
</svg>"""

AXIS_SVG = """<svg viewBox="0 0 560 210" role="img" aria-label="The same two numbers, 50 and 55, drawn with an honest axis starting at 0 and a misleading axis starting at 45" style="width:100%;max-width:560px;color:var(--ink)">
<g font-size="13" fill="currentColor" text-anchor="middle"><text x="140" y="18">Axis starts at 0 (honest)</text><text x="420" y="18">Axis starts at 45 (misleading)</text></g>
<line x1="40" y1="180" x2="250" y2="180" stroke="currentColor" stroke-opacity=".4"/>
<rect x="70" y="80" width="60" height="100" fill="var(--navy)" opacity=".75"/><rect x="150" y="70" width="60" height="110" fill="var(--accent)" opacity=".85"/>
<line x1="320" y1="180" x2="530" y2="180" stroke="currentColor" stroke-opacity=".4"/>
<rect x="350" y="130" width="60" height="50" fill="var(--navy)" opacity=".75"/><rect x="430" y="80" width="60" height="100" fill="var(--accent)" opacity=".85"/>
<g font-size="12" fill="currentColor" text-anchor="middle"><text x="100" y="198">A: 50</text><text x="180" y="198">B: 55</text><text x="380" y="198">A: 50</text><text x="460" y="198">B: 55</text></g>
</svg>"""

L = []

# ---------------------------------------------------------------- Center and spread
L.append({"id": "mean-median-mode-and-range", "title": "Mean, median, mode and spread", "band": "Grades 7–8", "minutes": 32,
 "lede": "One number to describe the middle of your data, another to describe how spread out it is, and why picking the wrong one lets people lie with true numbers.",
 "sections": [
  T("## Center: three ways to say \"typical\"\n| Measure | How to find it | Best for |\n|---|---|---|\n| **Mean** (average) | add everything, divide by how many | data without extreme values |\n| **Median** | the middle value once sorted | data with outliers or skew |\n| **Mode** | the most common value | categories, most popular choice |\n\nFor an even number of values, the median is the **mean of the two middle values**: the median of 3, 5, 8, 10 is (5 + 8) ÷ 2 = **6.5**."),
  E("Mean vs median when one value is extreme", "Ten people are in a room. Nine earn $50,000 a year. One earns $10,000,000.",
    ["Mean = (9 × 50,000 + 10,000,000) ÷ 10 = 10,450,000 ÷ 10 = **$1,045,000**.", "Median: sort the incomes. The 5th and 6th values are both $50,000, so the median is **$50,000**."],
    "The mean says the typical person is a millionaire. The median says $50,000, which is true for 9 out of 10 people. **Outliers drag the mean; they barely move the median.** That's why government reports use *median* household income."),
  CHECK("Home prices on a street: $210k, $220k, $230k, $240k, $1.9M. Which number best describes a typical home?", ["The mean, about $560k", "The median, $230k", "The mode", "The range"], 1,
        "One mansion drags the mean way up. The **median** ($230k) reflects what most homes cost."),
  T("## Spread: how much the data varies\nTwo teams can have the same average score and be completely different. Team A scores 50, 50, 50. Team B scores 0, 50, 100. Same mean, very different reliability. You need a measure of **spread**:\n\n- **Range** = max − min. Quick, but one outlier wrecks it.\n- **Interquartile range (IQR)** = Q3 − Q1, the spread of the **middle half** of the data. Resistant to outliers. Pairs with the median.\n- **Mean absolute deviation (MAD)** = the average distance of each value from the mean. Pairs with the mean.\n\nIn high school and college you'll meet **standard deviation**, the big brother of MAD. Same idea: how far values typically sit from the mean."),
  E("Find the IQR", "Data (already sorted): 3, 5, 7, 8, 9, 11, 13, 15",
    ["Median: 8 values, so average the 4th and 5th: (8 + 9) ÷ 2 = **8.5**.", "Lower half: 3, 5, 7, 8 → **Q1** = (5 + 7) ÷ 2 = 6.", "Upper half: 9, 11, 13, 15 → **Q3** = (11 + 13) ÷ 2 = 12.", "IQR = 12 − 6 = 6."],
    "**IQR = 6.** The middle half of the data spans 6 units."),
  E("Find the MAD", "Data: 2, 4, 6, 8",
    ["Mean = 20 ÷ 4 = 5.", "Distances from 5: 3, 1, 1, 3.", "Average distance = 8 ÷ 4 = 2."],
    "**MAD = 2.** On average, each value sits 2 away from the mean."),
  T("## Spotting outliers\nA standard rule: a value is an **outlier** if it's more than **1.5 × IQR** below Q1 or above Q3.\n\nFor the data above (Q1 = 6, Q3 = 12, IQR = 6): 1.5 × 6 = 9. Anything below 6 − 9 = **−3** or above 12 + 9 = **21** is an outlier. None here."),
  T("## Weighted averages\nWhen values don't all count equally, **weight** them: multiply each by its weight, add, divide by the total weight.\n\nYou buy fuel twice: 100 gallons at $4.00 and 300 gallons at $3.60. Your average price is **not** ($4.00 + $3.60) ÷ 2 = $3.80.\n\n(100 × 4.00 + 300 × 3.60) ÷ 400 = (400 + 1,080) ÷ 400 = **$3.70**. The cheaper fill-up counts three times as much because you bought three times as much."),
  E("What do I need to hit my average?", "Your first three test scores are 80, 90 and 70. What do you need on the fourth to average 85?",
    ["Target total for 4 tests: 4 × 85 = 340.", "Current total: 80 + 90 + 70 = 240.", "Needed: 340 − 240 = 100."], "**100.** Working backward from the total is faster than guessing."),
  T("## In your trading journal\nThese tools answer real questions:\n\n- **Mean R per trade** tells you if your system makes money.\n- **Median R** tells you what a *typical* trade looks like. In a big-R strategy, most trades lose 1R, so the median is often **−1R** even when the mean is positive. That's normal and it's exactly why the mean, not your gut, decides whether the system works.\n- **Spread** tells you how bumpy the ride is. A high-spread system needs smaller risk per trade to survive the streaks."),
  N("Common traps", "- **\"Average\" in the news** is usually the mean. Ask: would the median tell a different story?\n- **The median of an even-count list** is the average of the two middle values, which might not be in the data at all.\n- **Averaging averages** is wrong when the groups have different sizes. Use a weighted average.")
 ],
 "practice": [
  NUM("Mean of 4, 8, 15, 16, 23, 42?", 18, "Sum = 108. 108 ÷ 6 = 18."),
  NUM("Median of 7, 1, 9, 3, 5?", 5, "Sort: 1, 3, 5, 7, 9. The middle value is 5."),
  NUM("Median of 12, 4, 10, 6?", 8, "Sort: 4, 6, 10, 12. Average the middle two: (6 + 10) ÷ 2 = 8."),
  MC("Mode of: 2, 3, 3, 5, 7, 7, 7, 9?", ["3", "5", "7", "9"], 2, "7 appears three times, more than any other value."),
  NUM("Range of 15, 3, 22, 8, 11?", 19, "Max − min = 22 − 3 = 19."),
  MC("A data set has one huge outlier. Which measure of center is most **resistant** to it?", ["Mean", "Median", "Range", "Sum"], 1, "The median depends only on the middle position."),
  NUM("Mean absolute deviation of 1, 3, 5, 7?", 2, "Mean = 4. Distances: 3, 1, 1, 3. Average = 8 ÷ 4 = 2."),
  NUM("You need an average of 80 on 5 tests. Your first four are 75, 85, 70 and 82. What do you need on the fifth?", 88, "5 × 80 = 400. 75 + 85 + 70 + 82 = 312. 400 − 312 = 88."),
  NUM("Fuel: 50 gallons at $4.20 and 150 gallons at $3.80. Average price per gallon?", 3.90,
      "(50 × 4.20 + 150 × 3.80) ÷ 200 = (210 + 570) ÷ 200 = 780 ÷ 200 = **$3.90**.",
      level="challenge", hint="Weight each price by how many gallons you bought.", tol=0.001, unit="dollars",
      steps=["50 × 4.20 = 210.", "150 × 3.80 = 570.", "Total cost 780 for 200 gallons.", "780 ÷ 200 = 3.90."]),
  NUM("Data: 2, 4, 5, 7, 8, 10, 30. Using the 1.5 × IQR rule, what is the **upper fence** (values above it are outliers)?", 19,
      "Median = 7. Lower half 2, 4, 5 → Q1 = 4. Upper half 8, 10, 30 → Q3 = 10. IQR = 6. Upper fence = 10 + 1.5 × 6 = **19**. So 30 is an outlier.",
      level="challenge", hint="With 7 values, the median is the 4th; leave it out of both halves.",
      steps=["Median = 7 (4th value).", "Q1 = median of 2, 4, 5 = 4.", "Q3 = median of 8, 10, 30 = 10.", "IQR = 6. 1.5 × 6 = 9.", "Upper fence = 10 + 9 = 19."]),
  NUM("10 trades: 8 losses of −1R and 2 wins of +6R. What is the **mean** R per trade?", 0.4,
      "Total = 8 × (−1) + 2 × 6 = −8 + 12 = +4R. Mean = 4 ÷ 10 = **+0.4R**. Note the **median** is −1R: the typical trade loses, yet the system makes money.",
      level="challenge", hint="Add up all the R, then divide by the number of trades.", tol=0.001, unit="R"),
  MC("A company says \"Our average employee earns $95,000.\" Most workers earn about $40,000. What's most likely going on?", ["They're lying", "A few very high salaries pull the mean above the median", "The mode is $95,000", "The range is $95,000"], 1,
     "A handful of executive salaries can drag the **mean** far above what a typical worker earns. Ask for the **median**.",
     level="challenge", hint="Which measure of center do outliers drag?"),
 ],
 "sources": [STATS, CMATH]})

# ---------------------------------------------------------------- Data displays
L.append({"id": "reading-and-making-data-displays", "title": "Reading and making data displays", "band": "Grades 7–8", "minutes": 30,
 "lede": "Which chart fits which data, how to read box plots and scatter plots in seconds, and how to catch a graph that's lying to you.",
 "sections": [
  T("## Pick the display that fits the question\n| You want to show… | Use |\n|---|---|\n| Compare categories (sales by region) | **bar chart** |\n| How a number changes over time | **line graph** |\n| The shape of one set of numbers (how often each range occurs) | **histogram** or **dot plot** |\n| A quick summary of center and spread, or compare groups | **box plot** |\n| Whether two numbers move together | **scatter plot** |\n| Parts of a whole (only when parts add to 100%) | pie chart, though a bar chart usually reads better |"),
  T("## Bar chart vs histogram\nThey look alike but answer different questions:\n\n- **Bar chart**: separate **categories** (Ford, Kenworth, Peterbilt). Gaps between bars. Order doesn't matter.\n- **Histogram**: **number ranges** (loads that paid $0–$500, $500–$1,000...). Bars touch, because the ranges are continuous. Order matters.\n\nA histogram shows the **shape** of data: symmetric (bell-shaped), **skewed right** (a long tail of big values, like incomes), or skewed left."),
  T("## Box plots: five numbers in one picture\nA box plot draws the **five-number summary**: minimum, Q1, median, Q3, maximum. The box holds the middle half of the data (the IQR); the whiskers reach the extremes."),
  FIG(BOX_SVG, "The data 3, 5, 7, 8, 9, 11, 13, 15 as a box plot. The box spans Q1 to Q3; the line inside is the median."),
  T("How to read one fast:\n- **Where's the median line?** That's the center.\n- **How wide is the box?** That's the spread of the typical values.\n- **Is the median off-center or one whisker much longer?** The data is skewed toward the long side.\n- **Comparing two box plots?** Compare medians first, then box widths."),
  CHECK("In a box plot, what fraction of the data falls inside the box?", ["About a quarter", "About half", "About three quarters", "All of it"], 1, "The box runs from Q1 to Q3: the middle **50%**."),
  T("## Scatter plots and correlation\nA scatter plot puts one variable on each axis and a dot for each case. Look for:\n\n- **Positive correlation**: dots rise left to right (more miles → more fuel).\n- **Negative correlation**: dots fall (more sleep → fewer mistakes).\n- **No correlation**: a shapeless cloud.\n- **Strength**: how tightly the dots hug a line.\n\nA **line of best fit** summarizes the trend and lets you estimate values you didn't measure."),
  T("## Correlation is not causation\nIce cream sales and drownings rise together. Ice cream doesn't cause drowning; **summer** causes both. A hidden third factor like that is a **confounding variable**.\n\nBefore believing \"X causes Y,\" ask:\n1. Could Y cause X instead?\n2. Could a third thing cause both?\n3. Could it be coincidence? (With enough data, some random things always line up.)\n\nOnly a **controlled experiment**, where you change X on purpose and hold everything else steady, can show cause."),
  T("## How graphs lie with true numbers\nThe numbers below are identical. Only the axis changed."),
  FIG(AXIS_SVG, "Company B is 10% bigger than A. Cutting off the bottom of the axis makes it look twice as big."),
  T("Watch for:\n- **A y-axis that doesn't start at 0** on a bar chart. Bar length is supposed to show size.\n- **Uneven intervals** on an axis.\n- **3-D effects or pictures** scaled in two directions: doubling an icon's height *and* width makes it look **4 times** bigger.\n- **Cherry-picked time windows**: start a chart at the bottom of a crash and anything looks like a rally.\n- **No labels or units.** If you can't tell what's measured, you can't trust it.\n\n(Line graphs of things like stock prices can fairly start above 0. The rule is strictest for **bars**, whose length *is* the message.)"),
  N("Common traps", "- **Pie charts with too many slices** are unreadable. Use bars.\n- **A trend line doesn't promise the future.** Extending it far past your data (extrapolating) is a guess.\n- **Big samples aren't automatically good samples.** 10,000 people answering an online poll aren't a random sample of anything.")
 ],
 "practice": [
  MC("Best display for monthly revenue over two years?", ["Pie chart", "Line graph", "Box plot", "Bar chart of categories"], 1, "Change over time → **line graph**."),
  MC("A histogram's bars touch because…", ["it saves space", "the ranges on the x-axis are continuous", "the data is categories", "it's a style choice"], 1, "Histograms show number ranges that run into each other."),
  MC("A box plot shows: min 10, Q1 20, median 25, Q3 40, max 70. What is the IQR?", ["15", "20", "30", "60"], 1, "IQR = Q3 − Q1 = 40 − 20 = 20."),
  MC("In that same box plot, the data is…", ["skewed right (long tail of high values)", "skewed left", "perfectly symmetric", "impossible to tell"], 0, "The right whisker (40 → 70) is much longer than the left (10 → 20), and the median sits left of center in the box."),
  MC("Hours studied vs test score: the dots rise from lower left to upper right. This is…", ["negative correlation", "positive correlation", "no correlation", "causation"], 1, "Both go up together."),
  MC("Towns with more firefighters have more fire damage. The most likely explanation:", ["Firefighters cause damage", "Bigger towns have both more firefighters and more fires", "It's random", "Damage causes firefighters"], 1, "**Town size** is a confounding variable driving both."),
  MC("A bar chart's y-axis starts at 90. Bar A = 95, Bar B = 100. How many times taller does B **look** than A?", ["1.05", "2", "5", "10"], 1, "Visible heights: 95 − 90 = 5 and 100 − 90 = 10. B looks **twice** as tall though it's only about 5% bigger."),
  MC("Which display best compares the spread of delivery times for three drivers?", ["Three box plots side by side", "A pie chart", "A single line graph", "A table of names"], 0, "Box plots are built for comparing center and spread across groups."),
  MC("An ad shows a bag of money twice as tall **and** twice as wide to show profits doubled. What does the picture suggest?", ["Profits doubled", "Profits roughly quadrupled", "Profits rose 50%", "Nothing; it's accurate"], 1,
     "Area grows with height × width: 2 × 2 = 4. The eye reads area, so it looks **4 times** bigger, double the truth.",
     level="challenge", hint="What happens to area if both dimensions double?"),
  MC("A study finds people who drink coffee live longer. Which follow-up would best test whether coffee **causes** it?", ["Survey more coffee drinkers", "Randomly assign people to drink coffee or not, then follow them", "Ask people how they feel", "Compare coffee prices"], 1,
     "Only **random assignment** balances hidden factors (income, health habits) between groups, so differences can be blamed on coffee.",
     level="challenge", hint="How do you rule out confounding variables?"),
  MC("Your trade results histogram: a tall bar at −1R and a few small bars far out at +8R to +12R. The distribution is…", ["skewed left", "skewed right", "symmetric", "uniform"], 1,
     "The long tail points toward the **high** values, so it's **skewed right**. Big-R systems look like this: many small losses, a few huge wins. Mean > median.",
     level="challenge", hint="Which direction does the long tail point?"),
  MC("A scatter plot of truck age vs repair cost shows a strong positive trend for trucks aged 1–8 years. What's the riskiest use of the trend line?", ["Estimating cost for a 5-year-old truck", "Estimating cost for a 25-year-old truck", "Describing the trend", "Comparing two 6-year-old trucks"], 1,
     "25 years is far outside the data. **Extrapolating** assumes the pattern holds where you never measured it.",
     level="challenge", hint="Which estimate goes beyond the data you have?"),
 ],
 "sources": [STATS, CMATH]})

# ---------------------------------------------------------------- Probability basics
L.append({"id": "probability-basics", "title": "Probability basics", "band": "Grades 7–8", "minutes": 30,
 "lede": "Probability is the math of uncertainty. Learn to count outcomes, tell theory from experience, and spot the gambler's fallacy, the most expensive mistake in trading.",
 "sections": [
  T("## The probability scale\nProbability measures how likely something is, from **0** (impossible) to **1** (certain). You'll see it as a fraction, decimal or percent: 1/4 = 0.25 = 25%.\n\nWhen all outcomes are equally likely:\n\n**P(event) = number of favorable outcomes ÷ total number of outcomes**\n\nThe list of all possible outcomes is the **sample space**. A die's sample space is {1, 2, 3, 4, 5, 6}, so P(rolling a 5) = 1/6."),
  E("Two dice", "Roll two dice. What's the probability the sum is 7?",
    ["Sample space: 6 × 6 = 36 equally likely outcomes.", "Sums of 7: (1,6) (2,5) (3,4) (4,3) (5,2) (6,1) = 6 outcomes.", "P = 6 ÷ 36 = 1/6."],
    "**1/6.** Seven is the most likely sum. A sum of 2 needs (1,1): only 1/36."),
  T("## The complement\nThe **complement** of an event is \"it doesn't happen.\" Since something must happen:\n\n**P(not A) = 1 − P(A)**\n\nIf there's a 30% chance of rain, there's a 70% chance of no rain. This looks trivial. It's actually one of the most powerful tools in probability, because \"not\" is often far easier to count. You'll see that in the next lesson."),
  CHECK("A bag has 3 red, 5 blue and 2 green marbles. P(not blue)?", ["5/10", "1/2", "3/10", "1/5"], 1, "P(blue) = 5/10. P(not blue) = 1 − 5/10 = **5/10 = 1/2**."),
  T("## Theoretical vs experimental\n- **Theoretical probability** comes from reasoning: a fair coin lands heads with probability 1/2.\n- **Experimental probability** comes from data: flip 100 times, get 58 heads, so the experimental probability is 58/100 = 0.58.\n\nThey rarely match exactly in small samples. The **law of large numbers** says that as the number of trials grows, the experimental result gets closer to the true probability. Ten flips can easily give 70% heads. Ten thousand flips will land very close to 50%.\n\nThis is why one week of trading tells you almost nothing about your win rate, and 200 trades tell you a lot."),
  T("## The gambler's fallacy\nA coin lands heads 5 times in a row. What's P(heads) on the next flip?\n\n**Still 1/2.** The coin has no memory. Each flip is **independent**.\n\nThe **gambler's fallacy** is believing a streak makes the opposite result \"due.\" It's how people lose fortunes at roulette, and it's how traders blow up accounts: *\"I've lost four in a row, the next one has to win,\"* then doubling size.\n\nThe law of large numbers doesn't work by **correcting** streaks. It works by **drowning them out** with thousands more trials."),
  CHECK("You've lost 4 trades in a row. Your system historically wins 40% of trades, and each trade is independent. The chance your next trade wins is…", ["higher than 40%: you're due", "40%", "lower than 40%: you're cold", "0%"], 1, "Independent trades have no memory. It's **40%**, the same as always. That's why your plan uses fixed risk, not \"make it back\" sizing."),
  T("## Odds vs probability\nThey're not the same thing:\n\n- **Probability** = favorable ÷ **total**. P(rolling a 6) = 1/6.\n- **Odds in favor** = favorable : **unfavorable**. Odds of rolling a 6 = **1 : 5**.\n\nSportsbooks and casinos quote **odds**, often against you. To convert odds of a : b in favor into probability: **a ÷ (a + b)**. Odds of 1 : 3 → probability 1/4 = 25%."),
  E("Simulated vs exact", "A spinner has 4 equal sections: red, blue, green, yellow. You spin 20 times and get red 8 times.",
    ["Theoretical P(red) = 1/4 = 0.25.", "Experimental P(red) = 8/20 = 0.40.", "20 spins is a small sample, so a big gap isn't surprising."],
    "Expect the experimental number to move **toward 0.25** as you spin hundreds of times. If after 1,000 spins it's still near 0.40, the spinner is probably not fair."),
  N("Common traps", "- **Equally likely only applies when it's true.** \"I either win the lottery or I don't\" is two outcomes, but they're not 50/50.\n- **Probability can't be negative or above 1.** If you get 1.2, something's wrong.\n- **Rare events happen all the time** across enough tries. A one-in-a-million event happens to about 330 people a day in a country of 330 million.")
 ],
 "practice": [
  MC("P(rolling an even number on one die)?", ["1/6", "1/3", "1/2", "2/3"], 2, "Evens: 2, 4, 6 → 3 out of 6."),
  NUM("A deck has 52 cards, 4 of them aces. P(drawing an ace), as a decimal to 3 places?", 0.077, "4 ÷ 52 ≈ 0.077.", tol=0.0006),
  NUM("Weather says 35% chance of rain. P(no rain), as a percent?", 65, "1 − 0.35 = 0.65 = 65%.", unit="%"),
  NUM("Roll two dice. How many outcomes are in the sample space?", 36, "6 × 6 = 36."),
  MC("P(sum of 12 with two dice)?", ["1/6", "1/12", "1/36", "1/18"], 2, "Only (6,6) → 1 of 36."),
  NUM("You flip a coin 50 times and get 31 heads. Experimental P(heads), as a decimal?", 0.62, "31 ÷ 50 = 0.62.", tol=0.001),
  MC("A fair coin landed tails 6 times in a row. P(tails) next flip?", ["Less than 1/2", "1/2", "More than 1/2", "1/64"], 1, "Independent flips. The coin has no memory."),
  MC("The odds in favor of an event are 2 : 3. Its probability is…", ["2/3", "2/5", "3/5", "1/3"], 1, "a ÷ (a + b) = 2 ÷ 5."),
  NUM("Roll two dice. P(the sum is 8)? Give a fraction's decimal to 3 places.", 0.139,
      "Sums of 8: (2,6) (3,5) (4,4) (5,3) (6,2) = 5 outcomes. 5 ÷ 36 ≈ **0.139**.",
      level="challenge", hint="List every ordered pair that adds to 8. (3,5) and (5,3) are different outcomes.", tol=0.0006),
  MC("A trader says: \"I've had 5 winners in a row, so I'll size down. A loss is coming.\" If trades are independent, this is…", ["smart risk management", "the gambler's fallacy in reverse", "the law of large numbers", "correct because of averages"], 1,
     "Streaks don't make the other outcome **due**, in either direction. Sizing by streaks is the same fallacy. (Sizing down because you're tired or tilted is a different and valid reason.)",
     level="challenge", hint="Does the next trade know about the last five?"),
  NUM("A coin is flipped 3 times. How many outcomes in the sample space have **exactly 2 heads**?", 3,
      "HHT, HTH, THH. Three of the 8 possible outcomes.",
      level="challenge", hint="Write out all 8 outcomes (HHH, HHT, ...) and count."),
  MC("Your system's backtest shows 38% wins over 400 trades. Your first live week shows 2 wins in 10 trades (20%). Best conclusion?", ["The system is broken", "10 trades is too small a sample to tell; keep following the rules and track more", "The backtest was wrong", "Switch to a new system"], 1,
     "By the **law of large numbers**, 10 trades swing wildly. Even at a true 38% rate, 2 or fewer wins in 10 happens about 1 time in 5. Judge the system on hundreds of trades.",
     level="challenge", hint="How many trials does the law of large numbers need?"),
 ],
 "sources": [CMATH, STATS]})

# ---------------------------------------------------------------- Compound probability and expected value
L.append({"id": "compound-probability-and-expected-value", "title": "Compound probability and expected value", "band": "Grades 7–8", "minutes": 34,
 "lede": "And, or, at least one, and what you can expect to win or lose on average. The math casinos, insurers and professional traders live by.",
 "sections": [
  T("## AND: multiply (for independent events)\nTwo events are **independent** if one happening doesn't change the odds of the other: separate coin flips, separate dice, separate trades.\n\n**P(A and B) = P(A) × P(B)**\n\nP(two heads in a row) = 1/2 × 1/2 = **1/4**. P(three in a row) = 1/8. Each extra \"and\" makes the outcome **less** likely, fast."),
  E("Losing streaks", "Your system loses 60% of trades. What's the chance of 5 losses in a row?",
    ["Each trade is independent, so multiply: 0.6 × 0.6 × 0.6 × 0.6 × 0.6 = 0.6⁵.", "0.6⁵ = 0.07776."],
    "**About 7.8%**, roughly 1 in 13 stretches of five trades. Over a few hundred trades, a 5-loss streak is almost guaranteed. That's why your plan stops you at 2 losses a day and sizes so you can survive streaks."),
  T("## Dependent events: when the first changes the second\nDraw two cards **without putting the first back**. Now the second draw depends on the first.\n\nP(two aces) = P(ace first) × P(ace second, given an ace was taken)\n= 4/52 × 3/51 = 12/2,652 = **1/221** ≈ 0.45%\n\nWith replacement it would be 4/52 × 4/52 = 1/169. Small difference here, huge difference in small groups."),
  T("## OR: add, then subtract the overlap\n**P(A or B) = P(A) + P(B) − P(A and B)**\n\nWhy subtract? Anything that is **both** A and B got counted twice.\n\nP(drawing a heart **or** a king) = 13/52 + 4/52 − 1/52 = **16/52 = 4/13**. The king of hearts was in both groups.\n\nIf A and B **can't both happen** (rolling a 2 or a 5 on one die), the overlap is 0, and you just add."),
  CHECK("P(rolling a 1 or a 6 on one die)?", ["1/36", "1/6", "1/3", "1/2"], 2, "They can't both happen, so just add: 1/6 + 1/6 = **1/3**."),
  T("## At least one: use the complement\n\"At least one\" problems are a trap if you try to count every way it can happen. Flip it:\n\n**P(at least one) = 1 − P(none)**\n\nThis is the problem that **started probability theory**. In 1654 a gambler, the Chevalier de Méré, asked Blaise Pascal why betting on at least one 6 in 4 rolls of a die won money, but betting on at least one double-6 in 24 rolls of two dice lost. Pascal worked it out in letters with Pierre de Fermat."),
  E("De Méré's first bet", "P(at least one 6 in 4 rolls)?",
    ["P(no 6 on one roll) = 5/6.", "P(no 6 in 4 rolls) = (5/6)⁴ = 625/1,296 ≈ 0.482.", "P(at least one 6) = 1 − 0.482 = 0.518."],
    "**About 51.8%**: a small edge for the bettor. The double-6 bet comes out to about 49.1%, a small edge **against**. Tiny edges, repeated, decide who wins."),
  T("## Tree diagrams\nFor multi-step problems, draw a **tree**: each branch is an outcome with its probability. **Multiply along a path** to get that path's probability; **add across paths** that give the result you want. Every set of branches from one point must add to 1. When problems get confusing, the tree keeps you honest."),
  T("## Expected value: the average result per try\n**Expected value (EV) = Σ (probability × payoff)** over every outcome. It's what you'd average per try over the long run.\n\n**American roulette**, $1 on a single number: 38 pockets, pays 35 to 1.\n\nEV = (1/38)(+35) + (37/38)(−1) = (35 − 37) ÷ 38 = **−$0.053**\n\nYou lose about 5.3 cents per dollar, on average, forever. Casinos don't need luck. They need EV and volume."),
  T("## Expected value in trading\nYour plan's math is an expected-value calculation. Measured in **R** (your risk per trade):\n\n**EV per trade = (win rate × average win) − (loss rate × average loss)**\n\n| Win rate | Avg win | Avg loss | EV per trade |\n|---|---|---|---|\n| 50% | 1R | 1R | 0 |\n| 40% | 2R | 1R | 0.8 − 0.6 = **+0.2R** |\n| 25% | 10R | 1R | 2.5 − 0.75 = **+1.75R** |\n| 60% | 0.5R | 1R | 0.3 − 0.4 = **−0.1R** |\n\nThe last row is the trap: a 60% win rate that **loses money**. Win rate alone means nothing. Only EV matters.\n\nAt +1.75R per trade, risking $200, the long-run average is about **+$350 per trade**. But that average is built from a lot of −$200 days and a few huge ones. EV tells you the destination, not how smooth the road is."),
  CHECK("A system wins 70% of the time. Average win +$100, average loss −$300. EV per trade?", ["+$40", "−$20", "+$70", "−$90"], 1, "0.7 × 100 − 0.3 × 300 = 70 − 90 = **−$20**. A high win rate, losing money."),
  N("Common traps", "- **Multiplying non-independent events as if they were independent.** Two trades in the same direction on the same news aren't independent.\n- **Forgetting to subtract the overlap** in OR problems.\n- **Treating EV as a promise.** Positive EV wins over many trials. Over 10 trades, anything can happen. Size so you survive long enough for the average to show up.")
 ],
 "practice": [
  NUM("P(rolling two 6s with two dice), as a fraction 1/__? Type the denominator.", 36, "1/6 × 1/6 = 1/36."),
  NUM("P(3 heads in a row with a fair coin), as a decimal?", 0.125, "(1/2)³ = 1/8 = 0.125.", tol=0.0001),
  MC("P(heart or king) from a standard deck?", ["17/52", "16/52", "13/52", "4/52"], 1, "13 + 4 − 1 (king of hearts counted twice) = 16."),
  NUM("P(at least one head in 3 coin flips), as a decimal?", 0.875, "1 − P(no heads) = 1 − (1/2)³ = 1 − 0.125 = 0.875.", tol=0.0001),
  NUM("A game costs $1. You win $5 with probability 0.1, otherwise nothing. EV of playing, in dollars? (Include the $1 cost.)", -0.5, "0.1 × 5 − 1 = 0.5 − 1 = −$0.50 per play.", tol=0.001, unit="dollars"),
  MC("Drawing 2 cards **without replacement**, the events are…", ["independent", "dependent", "impossible", "complementary"], 1, "The first draw changes what's left for the second."),
  NUM("System: 40% wins at +2R, 60% losses at −1R. EV per trade in R?", 0.2, "0.4 × 2 − 0.6 × 1 = 0.8 − 0.6 = +0.2R.", tol=0.001, unit="R"),
  NUM("A bag has 4 red and 6 blue marbles. Draw 2 without replacement. P(both red), as a fraction's decimal to 3 places?", 0.133, "4/10 × 3/9 = 12/90 = 2/15 ≈ 0.133.", tol=0.0006),
  NUM("Your system wins 25% of trades. P(8 losses in a row)? Round to 3 decimals.", 0.1,
      "P(loss) = 0.75. 0.75⁸ ≈ **0.100**, about 1 in 10. Over hundreds of trades, 8-loss streaks will happen several times. At $250 risk that's −$2,000, the whole Lucid max loss, unless your daily and weekly stops cut it off first.",
      level="challenge", hint="Multiply 0.75 by itself 8 times.", tol=0.0006,
      steps=["P(loss) = 1 − 0.25 = 0.75.", "0.75² = 0.5625. 0.75⁴ = 0.3164.", "0.75⁸ = 0.3164² ≈ 0.100."]),
  NUM("De Méré's second bet: P(at least one double-6 in 24 rolls of two dice)? Round to 3 decimals.", 0.491,
      "P(no double-6 per roll) = 35/36. P(none in 24) = (35/36)²⁴ ≈ 0.509. P(at least one) = 1 − 0.509 ≈ **0.491**: a losing bet.",
      level="challenge", hint="Use 1 − P(none). P(no double-6 on one roll) = 35/36.", tol=0.0015),
  NUM("A system wins 30% of trades at an average +4R and loses 70% at −1R. Risking $200 per trade, what's the EV per trade in **dollars**?", 100,
      "EV in R = 0.3 × 4 − 0.7 × 1 = 1.2 − 0.7 = 0.5R. 0.5 × $200 = **+$100** per trade on average.",
      level="challenge", hint="Find EV in R first, then multiply by the dollar value of 1R.", unit="dollars"),
  MC("An insurance policy costs $500 a year. It pays $50,000 if your truck is totaled, which has a 0.5% chance per year. From the buyer's side, the EV is…", ["+$250: a great deal", "−$250: you pay for peace of mind", "$0", "−$500"], 1,
     "EV = 0.005 × 50,000 − 500 = 250 − 500 = **−$250**. Insurance is negative EV for buyers on purpose; you pay to avoid a loss you couldn't survive. EV isn't the only thing that matters when one outcome would ruin you.",
     level="challenge", hint="Expected payout = probability × payout. Then subtract the cost."),
 ],
 "sources": [CMATH, STATS]})

save("math", L)
