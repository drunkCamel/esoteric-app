// src/services/birthdateService.js
export async function calculateName(first_name, surname, second_name, fullname) {
  const response = await fetch("http://localhost:8000/api/name/calculate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ first_name, surname, second_name, fullname }),
  });

  if (!response.ok) {
    const err = await response.json();
    throw new Error(err.detail || "API error");
  }

  return response.json();
}
