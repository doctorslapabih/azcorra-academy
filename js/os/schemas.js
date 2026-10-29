// Database definitions (carried over from Claude Change and Claude IQ, minus trucking fields).
const opt = (name, color) => ({ name, color });

export const DBS = {
  tasks: {
    title: "Tasks", icon: "✅", view: "board", groupBy: "Status", sort: ["Due", "asc"],
    props: [
      { name: "Task", type: "title" },
      { name: "Status", type: "status", options: [opt("Inbox", "gray"), opt("This Week", "blue"), opt("Waiting", "yellow"), opt("Someday", "brown"), opt("Done", "green")], default: "Inbox" },
      { name: "Priority", type: "select", options: [opt("🔥 Top 3", "red"), opt("Normal", "default")], default: "Normal" },
      { name: "Area", type: "select", options: [opt("Trading", "green"), opt("Health & MMA", "red"), opt("Personal", "purple"), opt("Paused", "gray")] },
      { name: "Due", type: "date" }
    ]
  },
  daily_log: {
    title: "Daily Log", icon: "📅", view: "table", sort: ["Date", "desc"],
    props: [
      { name: "Day", type: "title" },
      { name: "Date", type: "date" },
      { name: "Score", type: "formula", formula: "dailyScore" },
      { name: "Up by 7", type: "checkbox" },
      { name: "Run", type: "checkbox" },
      { name: "Breakfast", type: "checkbox" },
      { name: "Lunch", type: "checkbox" },
      { name: "Dinner", type: "checkbox" },
      { name: "Water", type: "checkbox" },
      { name: "Reading", type: "checkbox" },
      { name: "Technique / Strength", type: "checkbox" },
      { name: "Lights Out by 11", type: "checkbox" },
      { name: "Energy", type: "select", options: [opt("1", "red"), opt("2", "orange"), opt("3", "yellow"), opt("4", "green"), opt("5", "blue")] },
      { name: "Sleep (hrs)", type: "number" },
      { name: "Calories", type: "number" },
      { name: "Protein (g)", type: "number" },
      { name: "Trading P&L", type: "dollar" },
      { name: "Notes", type: "text" }
    ]
  },
  trading_calendar: {
    title: "Trading Calendar", icon: "🗓️", view: "calendar", dateProp: "Date", sort: ["Date", "desc"], template: "tradingDay",
    props: [
      { name: "Day", type: "title" },
      { name: "Date", type: "date" },
      { name: "Sessions", type: "multi", options: [opt("NY", "blue"), opt("Asia", "purple")] },
      { name: "Trades", type: "number" },
      { name: "P&L", type: "dollar" },
      { name: "R", type: "number" },
      { name: "Best Grade", type: "select", options: [opt("A+", "green"), opt("A", "blue"), opt("B", "yellow"), opt("C", "red"), opt("No trade", "gray")] },
      { name: "Day Type", type: "select", options: [opt("Trend", "green"), opt("Balanced", "orange"), opt("Expansion", "purple"), opt("Choppy", "red")] },
      { name: "Emotion", type: "select", options: [opt("Calm", "green"), opt("FOMO", "orange"), opt("Revenge", "red"), opt("Hesitant", "yellow")] },
      { name: "Followed Plan", type: "checkbox" },
      { name: "Rules Broken", type: "number" },
      { name: "Bias", type: "text" },
      { name: "Lesson", type: "text" }
    ]
  },
  reading_list: {
    title: "Reading List", icon: "📚", view: "board", groupBy: "Status",
    props: [
      { name: "Book", type: "title" },
      { name: "Author", type: "text" },
      { name: "Category", type: "select", options: [opt("Trading", "green"), opt("Business", "blue"), opt("Mindset", "purple"), opt("Fighting", "red"), opt("Other", "gray")] },
      { name: "Status", type: "status", options: [opt("Want to Read", "gray"), opt("Reading", "blue"), opt("Finished", "green")], default: "Want to Read" },
      { name: "Started", type: "date" },
      { name: "Finished", type: "date" },
      { name: "Key Takeaway", type: "text" }
    ]
  },
  weekly_review: {
    title: "Weekly Review", icon: "🔁", view: "table", sort: ["Week Of", "desc"],
    props: [
      { name: "Week", type: "title" },
      { name: "Week Of", type: "date" },
      { name: "Wins", type: "text" },
      { name: "What Slipped", type: "text" },
      { name: "Trading P&L", type: "dollar" },
      { name: "Training Days", type: "number" },
      { name: "Avg Daily Score", type: "number" },
      { name: "Top 3 This Week", type: "text" },
      { name: "Next Week Focus", type: "text" }
    ]
  },
  decisions: {
    title: "Decisions", icon: "🧠", view: "table", sort: ["Date", "desc"],
    props: [
      { name: "Decision", type: "title" },
      { name: "Date", type: "date" },
      { name: "Status", type: "select", options: [opt("Thinking", "yellow"), opt("Decided", "green"), opt("Revisit", "orange")] },
      { name: "Reversible?", type: "select", options: [opt("Yes → decide fast", "green"), opt("No → slow down", "red")] },
      { name: "Goal It Serves", type: "text" },
      { name: "Cost", type: "text" },
      { name: "Takes Away From", type: "text" },
      { name: "The Call", type: "text" }
    ]
  },
  notebook: {
    title: "Notebook", icon: "📜", view: "table", sort: ["Date", "desc"],
    props: [
      { name: "Entry", type: "title" },
      { name: "Date", type: "date" },
      { name: "Subject", type: "select", options: [opt("IQ & Reasoning", "brown"), opt("Mathematics", "blue"), opt("Vocabulary", "purple"), opt("Writing", "orange"), opt("Science", "green")] },
      { name: "Type", type: "select", options: [opt("Game", "gray"), opt("Lesson", "brown"), opt("Reading", "default"), opt("Chat", "gray"), opt("Note", "default")] },
      { name: "Score", type: "number" },
      { name: "Out Of", type: "number" },
      { name: "Accuracy", type: "formula", formula: "accuracy" },
      { name: "Missed On", type: "multi", options: [opt("Hidden lists", "orange"), opt("Step-by-step logic", "purple"), opt("Number patterns", "blue"), opt("Final-step math", "red"), opt("Timing traps", "yellow")] },
      { name: "Key lesson", type: "text" },
      { name: "Feedback", type: "text" },
      { name: "My notes", type: "text" }
    ]
  }
};

export const FORMULAS = {
  dailyScore: p => ["Up by 7", "Run", "Breakfast", "Lunch", "Dinner", "Water", "Reading", "Technique / Strength", "Lights Out by 11"].filter(k => p[k]).length + "/9",
  accuracy: p => (p["Out Of"] ? Math.round((p.Score || 0) / p["Out Of"] * 100) + "%" : "")
};

const DAY = { weekday: "short", month: "short", day: "numeric" };
export const TEMPLATES = {
  tradingDay: dateStr => {
    const d = new Date(dateStr + "T12:00:00");
    const trade = n => `<toggle heading="h3">\nTrade ${n}\n\n- <b>Session · Model · Grade:</b>\n- <b>Level:</b>\n- <b>Entry / Stop / Target:</b>\n- <b>Result:</b> \\_\\_\\_ R · \\$\\_\\_\\_\n- <b>Followed every step?</b>\n</toggle>`;
    return {
      props: { Day: d.toLocaleDateString("en-US", DAY).replace(",", ""), Date: dateStr, "Followed Plan": false },
      body: `## 🗺️ Pre-market\n\n- <b>Liquidity target:</b>\n- <b>Value area:</b> above / inside / below\n- <b>Gamma Flip:</b> above / below\n- <b>Bias:</b> Longs toward \\_\\_\\_ / Shorts toward \\_\\_\\_\n- <b>Stacked levels:</b>\n\n## 📊 Day type\n\nTrend · Balanced · Expansion · Choppy →\n\n## 🎯 Trades\n\n${trade(1)}\n\n${trade(2)}\n\n${trade(3)}\n\n## 🧠 Review\n\n- <b>Did well:</b>\n- <b>Rules broken:</b>\n- <b>Lesson:</b>\n- <b>Tomorrow I will:</b>`
    };
  }
};
