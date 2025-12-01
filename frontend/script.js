async function analyze() {
    const tasks = JSON.parse(document.getElementById("taskInput").value);

    const res = await fetch("/api/tasks/analyze/", {
        method: "POST",
        headers: { "Content-Type": "application/json"},
        body: JSON.stringify(tasks)
    });

    const data = await res.json();
    document.getElementById("output").innerHTML =
        data.map(t => `<p><strong>${t.title}</strong> → Score: ${t.score}</p>`).join("");
}
