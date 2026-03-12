CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    amount FLOAT,
    transaction_type VARCHAR(50),
    old_balance FLOAT,
    new_balance FLOAT,
    fraud_probability FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
