// src/Home.jsx
import { useState } from "react";
import { calculateBirthdate } from "./services/birthdateService";
import { calculateName } from "./services/nameService";

// Define your 4 sections/tabs here — expand as you add more
const TABS = ["Numerology", "Chinese", "Astrology", "Vedic Square",];

function Home() {
  // ── Inputs ──────────────────────────────────────────────
  const [day,   setDay]   = useState("");
  const [month, setMonth] = useState("");
  const [year,  setYear]  = useState("");

  const [first_name, setFirstName] = useState("");
  const [surname, setSurname] = useState("");
  const [second_name, setSecondName] = useState("");
  

  // ── Results & UI state ───────────────────────────────────
  const [birthdateResults, setBirthdateResults] = useState(null);  // null = results hidden
  const [nameResults,   setNameResults]   = useState(null);   // null = results hidden
  const [activeTab, setActiveTab] = useState("Numerology");
  const [loading,   setLoading]   = useState(false);
  const [error,     setError]     = useState(null);

  // ── Call birthdate endpoint ─────────────────────────────
  const handleBirthdateCalculate = async () => {
    setError(null);
    setLoading(true);
    try {
      const data = await calculateBirthdate(
        parseInt(day),
        parseInt(month),
        parseInt(year)
      );
      setBirthdateResults(data);       // ← unlocks the results window
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  };

  // ── Call name endpoint ─────────────────────────────
  const handleNamecalculate = async () => {
    setError(null);
    setLoading(true);
    try {
      const data = await calculateName(
        first_name,
        surname,
        second_name
      );
      setNameResults(data);       // ← unlocks the results window
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  };

  const handleAllCalculations = async () => {
    setError(null);
    setLoading(true);
    try {
      await Promise.all([
        handleBirthdateCalculate(),
        handleNamecalculate()
      ]);
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="App">
      <h1>Calculations</h1>

      {/* ── INPUT FORM ── */}
      <div>
        <input
          type="number"
          placeholder="Day"
          value={day}
          onChange={(e) => setDay(e.target.value)}
        />
        <input
          type="number"
          placeholder="Month"
          value={month}
          onChange={(e) => setMonth(e.target.value)}
        />
        <input
          type="number"
          placeholder="Year"
          value={year}
          onChange={(e) => setYear(e.target.value)}
        />
              <input
        type="text"
        placeholder="First Name"
        value={first_name}
        onChange={(e) => setFirstName(e.target.value)}
      />
      <input
        type="text"
        placeholder="Surname"
        value={surname}
        onChange={(e) => setSurname(e.target.value)}
      />
      <input
        type="text"
        placeholder="Second Name"
        value={second_name}
        onChange={(e) => setSecondName(e.target.value)}
      />
        <button onClick={handleAllCalculations} disabled={loading}>
          {loading ? "Calculating..." : "Calculate All"}
        </button>

        {error && <p style={{ color: "red" }}>{error}</p>}
      </div>


      {/* ── RESULTS WINDOW — only shown after Calculate is clicked ── */}
      {birthdateResults !== null && nameResults !== null && (
        <div style={{ marginTop: "2rem" }}>

          {/* TABS */}
          <div>
            {TABS.map((tab) => (
              <button
                key={tab}
                onClick={() => setActiveTab(tab)}
                style={{ fontWeight: activeTab === tab ? "bold" : "normal" }}
              >
                {tab}
              </button>
            ))}
          </div>

          {/* TAB CONTENT */}
          <div style={{ marginTop: "1rem" }}>

            {activeTab === "Chinese" && (
              <div>
                <h2>Chinese Calculations</h2>
                <p>Lo Shu Square: {Object.values(birthdateResults.lo_shu_square).join("/")}</p>
                <p>Chinese Zodiac Sign: {birthdateResults.chinese_zodiac_sign}</p>
                <p>Chinese Enemy Sign: {birthdateResults.chinese_enemy_sign}</p>
                <p>Chinese Friendly Sign 1: {birthdateResults.chinese_friendly_sign_one}</p>
                <p>Chinese Friendly Sign 2: {birthdateResults.chinese_friendly_sign_two}</p>
                <p>Current Chinese Zodiac Year: {birthdateResults.chinese_current_year_zodiac_sign}</p>

              </div>
            )}

            {activeTab === "Numerology" && (
              <div>
                <h2>Numerology</h2>
                <p>Life Path: {Object.values(birthdateResults.lifepath_number).join("/")}</p>
                <p>Pinnacles 1: {Object.values(birthdateResults.pinnacle_one).join("/")}</p>
                <p>Pinnacles 2: {Object.values(birthdateResults.pinnacle_two).join("/")}</p>
                <p>Pinnacles 3: {Object.values(birthdateResults.pinnacle_three).join("/")}</p>
                <p>Pinnacles 4: {Object.values(birthdateResults.pinnacle_fourth).join("/")}</p>
                <p>Personal Year: {Object.values(birthdateResults.personal_year).join("/")}</p>
                <p>Personal Month: {Object.values(birthdateResults.personal_month).join("/")}</p>
                <p>Cycle 1: {Object.values(birthdateResults.cycle_one).join("/")}</p>
                <p>Cycle 2: {Object.values(birthdateResults.cycle_two).join("/")}</p>
                <p>Cycle 3: {Object.values(birthdateResults.cycle_three).join("/")}</p>
                <p>Pythagoras Life Cycle: {Object.values(birthdateResults.pythagoras_life_cycle).join("/")}</p>
                <p>Periodical Challenge 1: {Object.values(birthdateResults.periodical_challenge_one).join("/")}</p>
                <p>Periodical Challenge 2: {Object.values(birthdateResults.periodical_challenge_two).join("/")}</p>
                <p>Periodical Challenge 3: {Object.values(birthdateResults.periodical_challenge_three).join("/")}</p>
                <p>Periodical Challenge 4: {Object.values(birthdateResults.periodical_challenge_four).join("/")}</p>
              </div>
            )}

            {activeTab === "Astrology" && (
              <div>
                <h2>Astrology</h2>
                <p>Zodiac Sign: {birthdateResults.zodiac_sign}</p>
              </div>
            )}

            {activeTab === "Combined" && (
              <div>
                <h2>Combined Calculations</h2>
                <p>Result: {birthdateResults.combined_result}</p>
              </div>
            )}

          </div>
        </div>
      )}
    </div>
  );
}

export default Home;
