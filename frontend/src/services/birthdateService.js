// src/services/birthdateService.js
export async function calculateBirthdate(day, month, year) {
  const response = await fetch("http://localhost:8000/api/birthdate/calculate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ day, month, year }),
  });

  if (!response.ok) {
    const err = await response.json();
    throw new Error(err.detail || "API error");
  }

  return response.json();
}
