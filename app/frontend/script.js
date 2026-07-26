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
