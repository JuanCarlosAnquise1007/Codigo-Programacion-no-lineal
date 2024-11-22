import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Función lineal
def f(x):
    return 3*x + 2

# Configuración de Streamlit
st.title("1: Convexidad de la función f(x) = 3x + 2")
x = np.linspace(-10, 10, 100)
y = f(x)

# Graficar
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="f(x) = 3x + 2")
plt.title("Función lineal y su convexidad")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.legend()
st.pyplot(plt)

def f(x):
    return x**3

def f_second_derivative(x):
    return 6*x

st.title("2: Convexidad de f(x) = x^3")
x = np.linspace(-2, 2, 100)
y = f(x)
second_derivative = f_second_derivative(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label="f(x) = x^3")
plt.plot(x, second_derivative, label="f''(x) = 6x", linestyle="--")
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.title("Convexidad y Concavidad de f(x) = x^3")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
st.pyplot(plt)

def f(x):
    return np.exp(2*x)

def f_second_derivative(x):
    return 4*np.exp(2*x)

st.title("3: Convexidad de f(x) = e^(2x)")
x = np.linspace(-2, 2, 100)
y = f(x)
second_derivative = f_second_derivative(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label="f(x) = e^(2x)")
plt.plot(x, second_derivative, label="f''(x) = 4e^(2x)", linestyle="--")
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.title("Convexidad de f(x) = e^(2x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
st.pyplot(plt)

def f(x):
    return np.log(x)

def f_second_derivative(x):
    return -1/x**2

st.title("4: Concavidad de f(x) = ln(x)")
x = np.linspace(0.1, 5, 100)
y = f(x)
second_derivative = f_second_derivative(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label="f(x) = ln(x)")
plt.plot(x, second_derivative, label="f''(x) = -1/x^2", linestyle="--")
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.title("Concavidad de f(x) = ln(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
st.pyplot(plt)

def f(x):
    return x**4 - 2*x**2 + 1

def f_second_derivative(x):
    return 12*x**2 - 4

st.title("5: Convexidad y Concavidad de f(x) = x^4 - 2x^2 + 1")
x = np.linspace(-2, 2, 100)
y = f(x)
second_derivative = f_second_derivative(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label="f(x) = x^4 - 2x^2 + 1")
plt.plot(x, second_derivative, label="f''(x) = 12x^2 - 4", linestyle="--")
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.title("Convexidad y Concavidad de f(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
st.pyplot(plt)
