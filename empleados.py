import streamlit as st
import pandas as pd

st.title("Registro de empleados")

# Sesión para guardar datos
if "empleados" not in st.session_state:
    st.session_state.empleados = []

with st.form("form"):
    nombre = st.text_input("Nombre")
    telefono = st.text_input("Teléfono")
    correo = st.text_input("Correo")
    submitted = st.form_submit_button("Guardar")
    if submitted:
        st.session_state.empleados.append({"Nombre": nombre, "Teléfono": telefono, "Correo": correo})
        st.success("Empleado registrado")

# Mostrar tabla
df = pd.DataFrame(st.session_state.empleados)
st.write("### Empleados registrados", df)

# Exportar
if not df.empty:
    st.download_button("📥 Exportar CSV", df.to_csv(index=False).encode("utf-8"), "empleados.csv", "text/csv")
