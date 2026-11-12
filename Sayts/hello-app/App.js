import React, { useState } from 'react';

export default function App() {
    // Результат:
    const [message, setMessage] = useState('');

    // showMessage():
    function showMessage() {
        setMessage('Hello world');
    }

    // GUI
    return (
        <div style={styles.container}>
            {/** Заголовок */}
            <div style={{ textAlign: 'center', marginBottom: 15 }}>
                <h1 style={{ color: 'purple' }}>
                    Проста програма
                </h1>

                <p style={{ color: 'navy' }}>
                    Натисніть кнопку, щоб побачити повідомлення
                </p>
            </div>

            {/** Кнопка */}
            <button
                style={styles.button}
                onClick={showMessage}
            >
                Натиснути
            </button>

            {/** Панель відображення результату */}
            {message !== '' && (
                <div style={{ marginTop: 15, textAlign: 'center' }}>
                    <p style={styles.message}>
                        {message}
                    </p>
                </div>
            )}
        </div>
    );
}

const styles = {
    container: {
        minHeight: '100vh',
        background: 'url("https://images.unsplash.com/photo-1500534623283-312aade485b7?auto=format&fit=crop&w=1920&q=80")',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'flex-start',
        paddingTop: 30,
        paddingLeft: 20,
        paddingRight: 20
    },

    button: {
        backgroundColor: 'lightgreen',
        borderRadius: 10,
        border: '2px solid green',
        padding: '12px 40px',
        fontSize: 16,
        cursor: 'pointer'
    },

    message: {
        fontSize: 24,
        fontWeight: 'bold',
        color: 'teal'
    }
};
