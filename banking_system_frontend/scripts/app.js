const API_BASE_URL = "http://localhost:5000";

const balanceElement = document.getElementById("balance");
const transactionsList = document.getElementById("transactions-list");
const noTransactionsMessage = document.getElementById("no-transactions-message");
const addTransactionBtn = document.getElementById("add-transaction-btn");
const modal = document.getElementById("modal");
const closeBtn = document.querySelector(".close-btn");
const transactionForm = document.getElementById("transaction-form");
const modalTitle = document.getElementById("modal-title");

let currentTransactionId = null;

// Fetch and display transactions
async function fetchTransactions() {
          const response = await fetch(`${API_BASE_URL}/transactions`);
          const transactions = await response.json();
          renderTransactions(transactions);
          updateBalance(transactions);
}

// Render transactions
function renderTransactions(transactions) {
          transactionsList.innerHTML = "";
          if (transactions.length === 0) {
                    noTransactionsMessage.style.display = "block";
          } else {
                    noTransactionsMessage.style.display = "none";
                    transactions.forEach(transaction => {
                              const transactionItem = document.createElement("div");
                              transactionItem.classList.add("transaction-item");

                              transactionItem.innerHTML = `
        <div class="transaction-header">
          <span class="transaction-type">${transaction.type}</span>
          <span class="transaction-amount">${transaction.amount}</span>
        </div>
        <div class="transaction-description">${transaction.description}</div>
        <div class="transaction-date">${new Date(transaction.date).toLocaleString()}</div>
        <div class="transaction-actions">
          <button onclick="editTransaction(${transaction.id})">Edit</button>
          <button onclick="deleteTransaction(${transaction.id})">Delete</button>
        </div>
      `;
                              transactionsList.appendChild(transactionItem);
                    });
          }
}

// Update balance
function updateBalance(transactions) {
          const balance = transactions.reduce((total, transaction) => {
                    return total + (transaction.type === "credit" ? transaction.amount : -transaction.amount);
          }, 0);
          balanceElement.textContent = `R ${balance.toFixed(2)}`;
}

// Add or edit transaction
async function saveTransaction(event) {
          event.preventDefault();
          const formData = new FormData(transactionForm);
          const transactionData = {
                    type: formData.get("type"),
                    amount: parseFloat(formData.get("amount")),
                    description: formData.get("description")
          };

          const url = currentTransactionId ? `${API_BASE_URL}/transactions/${currentTransactionId}` : `${API_BASE_URL}/transactions`;
          const method = currentTransactionId ? "PUT" : "POST";

          const response = await fetch(url, {
                    method,
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(transactionData)
          });

          if (response.ok) {
                    fetchTransactions();
                    closeModal();
          }
}

// Edit transaction
function editTransaction(id) {
          currentTransactionId = id;
          modalTitle.textContent = "Edit Transaction";
          fetch(`${API_BASE_URL}/transactions/${id}`)
                    .then(response => response.json())
                    .then(transaction => {
                              document.getElementById("type").value = transaction.type;
                              document.getElementById("amount").value = transaction.amount;
                              document.getElementById("description").value = transaction.description;
                              openModal();
                    });
}

// Delete transaction
async function deleteTransaction(id) {
          const response = await fetch(`${API_BASE_URL}/transactions/${id}`, { method: "DELETE" });
          if (response.ok) {
                    fetchTransactions();
          }
}

// Error handling for API requests
async function fetchTransactions() {
          try {
                    const response = await fetch(`${API_BASE_URL}/transactions`);
                    if (!response.ok) {
                              throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    const transactions = await response.json();
                    renderTransactions(transactions);
                    updateBalance(transactions);
          } catch (error) {
                    console.error("Error fetching transactions:", error);
                    alert("Failed to fetch transactions. Please try again.");
          }
}

async function saveTransaction(event) {
          event.preventDefault();
          const formData = new FormData(transactionForm);
          const transactionData = {
                    type: formData.get("type"),
                    amount: parseFloat(formData.get("amount")),
                    description: formData.get("description")
          };

          const url = currentTransactionId ? `${API_BASE_URL}/transactions/${currentTransactionId}` : `${API_BASE_URL}/transactions`;
          const method = currentTransactionId ? "PUT" : "POST";

          try {
                    const response = await fetch(url, {
                              method,
                              headers: { "Content-Type": "application/json" },
                              body: JSON.stringify(transactionData)
                    });

                    if (!response.ok) {
                              const errorData = await response.json();
                              throw new Error(errorData.message || "Failed to save transaction.");
                    }

                    fetchTransactions();
                    closeModal();
          } catch (error) {
                    console.error("Error saving transaction:", error);
                    alert(error.message);
          }
}

async function deleteTransaction(id) {
          try {
                    const response = await fetch(`${API_BASE_URL}/transactions/${id}`, { method: "DELETE" });
                    if (!response.ok) {
                              throw new Error("Failed to delete transaction.");
                    }
                    fetchTransactions();
          } catch (error) {
                    console.error("Error deleting transaction:", error);
                    alert("Failed to delete transaction. Please try again.");
          }
}

// Display error messages
function showError(message) {
          const errorMessage = document.getElementById("error-message");
          errorMessage.textContent = message;
          errorMessage.style.display = "block";
          setTimeout(() => {
                    errorMessage.style.display = "none";
          }, 5000);
}

async function fetchTransactions() {
          try {
                    const response = await fetch(`${API_BASE_URL}/transactions`);
                    if (!response.ok) {
                              throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    const transactions = await response.json();
                    renderTransactions(transactions);
                    updateBalance(transactions);
          } catch (error) {
                    console.error("Error fetching transactions:", error);
                    showError("Failed to fetch transactions. Please try again.");
          }
}


function openModal() {
          modal.style.display = "flex";
}


function closeModal() {
          modal.style.display = "none";
          transactionForm.reset();
          currentTransactionId = null;
          modalTitle.textContent = "Add Transaction";
}

// Event Listeners
addTransactionBtn.addEventListener("click", openModal);
closeBtn.addEventListener("click", closeModal);
transactionForm.addEventListener("submit", saveTransaction);

fetchTransactions();
