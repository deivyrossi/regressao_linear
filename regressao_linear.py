import numpy as np
import matplotlib.pyplot as plt

# --- 1. Entrada de Dados (Conforme Tabela do PDF) ---
# T = Temperatura (eixo x), L = Comprimento (eixo y)
T = np.array([20, 30, 40, 50, 60, 70, 80], dtype=float)
L = np.array([1000.0, 1000.3, 1000.6, 1000.9, 1001.2, 1001.5, 1001.8], dtype=float)

# --- 2. Implementação do Método dos Mínimos Quadrados ---
# Objetivo: Achar y = ax + b
n = len(T)

# Somatórios necessários para as fórmulas manuais
sum_x = np.sum(T)
sum_y = np.sum(L)
sum_xy = np.sum(T * L)
sum_x2 = np.sum(T ** 2)

# Cálculo dos coeficientes 'a' (inclinação) e 'b' (interseção)
# Fórmula: a = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - (sum_x)^2)
a_calc = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
b_calc = (sum_y - a_calc * sum_x) / n

print("--- RESULTADOS DA IMPLEMENTAÇÃO ---")
print(f"Modelo Calculado: L(T) = {a_calc:.4f}T + {b_calc:.4f}")

# --- 3. Comparação com Modelo Teórico ---
# Modelo esperado: L(T) = 0.03T + 999.4
a_teorico = 0.03
b_teorico = 999.4

print(f"Modelo Teórico:   L(T) = {a_teorico:.4f}T + {b_teorico:.4f}")

# Calcular erro absoluto entre os coeficientes
erro_a = abs(a_calc - a_teorico)
erro_b = abs(b_calc - b_teorico)
print(f"Diferença nos coeficientes: a={erro_a:.6f}, b={erro_b:.6f}")

# --- 4. Cálculo do R² (Coeficiente de Determinação) ---
# Valores preditos pelo nosso modelo calculado
L_pred = a_calc * T + b_calc

# Média dos dados originais (y barra)
L_media = np.mean(L)

# Soma dos Quadrados dos Resíduos (SS_res)
SS_res = np.sum((L - L_pred) ** 2)

# Soma Total dos Quadrados (SS_tot)
SS_tot = np.sum((L - L_media) ** 2)

# R²
R2 = 1 - (SS_res / SS_tot)

print(f"\n--- ANÁLISE ESTATÍSTICA ---")
print(f"Soma Quadrados Resíduos (SS_res): {SS_res:.6f}")
print(f"Coeficiente de Determinação (R²): {R2:.6f}")
print("Interpretação: Um R² de 1.0 indica um ajuste perfeito aos dados.")

# --- 5. Geração de Gráfico ---
plt.figure(figsize=(8, 6))
plt.scatter(T, L, color='blue', label='Dados Experimentais', zorder=5)
plt.plot(T, L_pred, color='red', linestyle='--', label=f'Reta Ajustada: {a_calc:.4f}T + {b_calc:.4f}')
plt.title('Regressão Linear: Dilatação Térmica da Barra')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Comprimento (mm)')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.savefig('grafico_regressao.png') # Salva a imagem para o relatório
plt.show()