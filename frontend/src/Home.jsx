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
                <p>Lo Shu Square: {JSON.stringify(birthdateResults.lo_shu_square)}</p>
                <p>Chinese Birthday: {JSON.stringify(birthdateResults.chinese_birth_day)}</p>
              </div>
            )}

            {activeTab === "Numerology" && (
              <div>
                <h2>Numerology</h2>
                <p>Life Path: {birthdateResults.life_path_number}</p>
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
