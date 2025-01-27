describe("Transaction Manager", () => {
          it("should display the account balance", () => {
                    cy.visit("/");
                    cy.contains("Account Balance").should("exist");
          });

          it("should add a new transaction", () => {
                    cy.visit("/");
                    cy.get("#add-transaction-btn").click();
                    cy.get("#type").select("credit");
                    cy.get("#amount").type("100");
                    cy.get("#description").type("Test Transaction");
                    cy.get("button[type='submit']").click();
                    cy.contains("Test Transaction").should("exist");
          });

          it("should edit a transaction", () => {
                    cy.visit("/");
                    cy.contains("Test Transaction").parent().find("button").contains("Edit").click();
                    cy.get("#description").clear().type("Updated Transaction");
                    cy.get("button[type='submit']").click();
                    cy.contains("Updated Transaction").should("exist");
          });

          it("should delete a transaction", () => {
                    cy.visit("/");
                    cy.contains("Updated Transaction").parent().find("button").contains("Delete").click();
                    cy.contains("Updated Transaction").should("not.exist");
          });
});