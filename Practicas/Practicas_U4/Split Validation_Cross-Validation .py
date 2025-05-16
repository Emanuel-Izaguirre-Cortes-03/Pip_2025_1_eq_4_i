import pandas as pd
from sklearn.model_selection import train_test_split, KFold, cross_val_score, cross_val_predict
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import warnings

# Ignorar las advertencias FutureWarning
warnings.filterwarnings("ignore", category=FutureWarning)
# Especifica la ruta a tu archivo Excel
ruta_excel = 'datos_proyectos.xlsx'  # Reemplaza con el nombre de tu archivo

# Lee el archivo Excel en un DataFrame de pandas
try:
    df = pd.read_excel(ruta_excel)
except FileNotFoundError:
    print(f"Error: No se encontró el archivo en la ruta: {ruta_excel}")
    exit()

# Imprime los nombres de las columnas para verificar
print("Nombres de las columnas en el DataFrame:")
print(df.columns)

# Separar las características (X) de la variable objetivo (y)
X = df[['Horas Trabajadas', 'Tareas Completadas', 'Miembros Equipo', 'Dias Restantes']]
y = df['Tipo de Proyecto']

# Codificar la variable objetivo (si no es numérica)
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

print("Características (X):\n", X.head())
print("\nVariable Objetivo Codificada (y_encoded):\n", y_encoded[:5])
print("\nClases originales:", label_encoder.classes_)

# --- Split Validation ---
X_train, X_val, y_train, y_val = train_test_split(X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded)

modelo_split = LogisticRegression(random_state=42, solver='liblinear', multi_class='auto')
modelo_split.fit(X_train, y_train)

y_pred_val = modelo_split.predict(X_val)
accuracy_val = accuracy_score(y_val, y_pred_val)
report_val = classification_report(y_val, y_pred_val, target_names=label_encoder.classes_)

print("\n--- Resultados de Split Validation ---")
print(f"Precisión en el conjunto de validación: {accuracy_val:.2f}")
print("\nReporte de clasificación en el conjunto de validación:\n", report_val)

# --- Cross-Validation (K-Fold) ---
modelo_cv = LogisticRegression(random_state=42, solver='liblinear', multi_class='auto')
kf = KFold(n_splits=5, shuffle=True, random_state=42)
scores_cv = cross_val_score(modelo_cv, X, y_encoded, cv=kf, scoring='accuracy')

print("\n--- Resultados de Cross-Validation (K-Fold) ---")
print("Puntuaciones de precisión en cada fold:", scores_cv)
print(f"Precisión promedio de validación cruzada: {scores_cv.mean():.2f}")
print(f"Desviación estándar de las puntuaciones: {scores_cv.std():.2f}")

y_pred_cv = cross_val_predict(modelo_cv, X, y_encoded, cv=kf)
report_cv = classification_report(y_encoded, y_pred_cv, target_names=label_encoder.classes_)
print("\nReporte de clasificación con Cross-Validation:\n", report_cv)