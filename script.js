async function addStudent() {
    const name = document.getElementById('student-name').value;
    const age = document.getElementById('student-age').value;

    const response = await fetch('/students', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ id: Date.now(), name, age })
    });

    const newStudent = await response.json();
    displayStudents();
}

async function displayStudents() {
    const response = await fetch('/students');
    const students = await response.json();

    const tableBody = document.querySelector('#students-table tbody');
    tableBody.innerHTML = '';
    
    students.forEach(student => {
        const row = `<tr>
            <td>${student.id}</td>
            <td>${student.name}</td>
            <td>${student.age}</td>
            <td><button onclick="deleteStudent(${student.id})">Delete</button></td>
        </tr>`;
        tableBody.innerHTML += row;
    });
}

async function deleteStudent(id) {
    await fetch(`/students/${id}`, { method: 'DELETE' });
    displayStudents();
}

// Initial load of students
displayStudents();
