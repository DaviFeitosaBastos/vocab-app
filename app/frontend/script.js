// ── Navigation ──
const navBtns = document.querySelectorAll(".nav-btn");
const screens = document.querySelectorAll(".screen");

navBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    const target = btn.dataset.screen;

    navBtns.forEach((b) => b.classList.remove("active"));
    screens.forEach((s) => s.classList.remove("active"));

    btn.classList.add("active");
    document.getElementById(`screen-${target}`).classList.add("active");
  });
});

// ── Search ──
const searchInput = document.getElementById("search-input");
const btnSearch = document.getElementById("btn-search");
const searchResult = document.getElementById("search-result");
const searchEmpty = document.getElementById("search-empty");

async function searchWord() {
  const term = searchInput.value.trim().toLowerCase();
  if (!term) return;

  // placeholder — will call pywebview.api.search_word(term) later
  console.log("searching:", term);
}

btnSearch.addEventListener("click", searchWord);
searchInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") searchWord();
});

// ── Daily Word ──
document.getElementById("btn-next").addEventListener("click", () => {
  // placeholder — will call pywebview.api.get_daily_word() later
  console.log("next word");
});

window.addEventListener('pywebviewready', loadDailyWord)

async function loadDailyWord() {
  const word = await window.pywebview.api.get_daily_word();
  if (!word) return;

  document.getElementById("daily-word").textContent = word.Word;
  document.getElementById("daily-pos").textContent = word.Meanings[0];
  document.getElementById("daily-definition").textContent = word.Meanings[1];

  const synonymsEl = document.getElementById("daily-synonyms");
  synonymsEl.innerHTML = word.Synonyms
    .slice(0, 4)
    .map((s) => `<span class="tag">${s}</span>`)
    .join("");
}


document.getElementById("btn-next").addEventListener("click", async () => {
    const word = await window.pywebview.api.get_daily_word()
    if (!word) return

    await window.pywebview.api.mark_as_seen(word.Id)

    document.getElementById("daily-word").textContent = word.Word
    document.getElementById("daily-pos").textContent = word.Meanings[0]
    document.getElementById("daily-definition").textContent = word.Meanings[1]

    const synonymsEl = document.getElementById("daily-synonyms")
    synonymsEl.innerHTML = word.Synonyms
        .slice(0, 4)
        .map(s => `<span class="tag">${s}</span>`)
        .join("")
})

async function searchWord() {
    const term = searchInput.value.trim().toLowerCase()
    if (!term) return

    const result = await window.pywebview.api.search_word(term)

    if (result) {
        searchResult.classList.remove("hidden")
        searchEmpty.classList.add("hidden")
        document.getElementById("result-word").textContent = result.Word
        document.getElementById("result-pos").textContent = result.Meanings[0]
        document.getElementById("result-definition").textContent = result.Meanings[1]
        document.getElementById("result-synonyms").innerHTML = result.Synonyms
            .slice(0, 4)
            .map(s => `<span class="tag">${s}</span>`)
            .join("")
    } else {
        searchResult.classList.add("hidden")
        searchEmpty.classList.remove("hidden")
    }
}

navBtns.forEach((btn) => {
  btn.addEventListener("click", async () => {
    const target = btn.dataset.screen;

    navBtns.forEach((b) => b.classList.remove("active"));
    screens.forEach((s) => s.classList.remove("active"));

    btn.classList.add("active");
    document.getElementById(`screen-${target}`).classList.add("active");

    if (target === "progress") {
        await loadProgress()
    }
  });
});

async function loadProgress() {
    const data = await window.pywebview.api.get_progress()

    document.getElementById("stat-seen").textContent = data.seen_count
    document.getElementById("stat-remaining").textContent = data.remaining
    document.getElementById("stat-percent").textContent = data.percent + "%"
    document.getElementById("progress-bar").style.width = data.percent + "%"

    const list = document.getElementById("progress-list")
    list.innerHTML = data.seen_words.map(word => `
        <div class="progress__item">
            <span class="progress__item-word">${word.Word}</span>
            <span class="progress__item-def">${word.Meanings[1]}</span>
        </div>
    `).join("")
}