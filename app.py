import streamlit as st
import pandas as pd

# Título de la aplicación
st.title('Aplicación para Contadores de Guatemala') 

# Sección para el cálculo de IVA
st.header('Cálculo de IVA (Impuesto al Valor Agregado)')
iva_rate = 0.12

# Entrada de datos para cálculo de IVA
ventas_brutas = st.number_input('Ventas Brutas (sin IVA)', min_value=0.0, format='%f')
compras_brutas = st.number_input('Compras Brutas (sin IVA)', min_value=0.0, format='%f')

# Cálculo del IVA
iva_ventas = ventas_brutas * iva_rate
iva_compras = compras_brutas * iva_rate
iva_a_pagar = iva_ventas - iva_compras

# Mostrar los resultados del IVA
st.write('IVA sobre Ventas: Q', iva_ventas)
st.write('IVA sobre Compras: Q', iva_compras)
st.write('IVA a pagar: Q', iva_a_pagar)

# Sección para el cálculo de ISR
st.header('Cálculo de ISR (Impuesto Sobre la Renta)')
st.write('ISR para régimen general: basado en tablas de la SAT Guatemala')

# Entrada de datos para cálculo de ISR
ingresos = st.number_input('Ingrese sus ingresos anuales', min_value=0.0, format='%f')
deducciones = st.number_input('Ingrese sus deducciones permitidas (gastos médicos, educación, etc.)', min_value=0.0, format='%f')

# Cálculo del ISR
base_imponible = ingresos - deducciones

if base_imponible <= 30000:
    isr = base_imponible * 0.05
elif base_imponible <= 60000:
    isr = 1500 + (base_imponible - 30000) * 0.10
else:
    isr = 4500 + (base_imponible - 60000) * 0.15

# Mostrar resultado del ISR
st.write('Base imponible: Q', base_imponible)
st.write('ISR a pagar: Q', isr)

# Sección para el simulador de préstamos
st.header('Simulador de Préstamos')
st.write('Ingrese los detalles del préstamo para calcular las cuotas.')

# Entrada de datos para simulador de préstamos
monto_prestamo = st.number_input('Monto del préstamo (Q)', min_value=0.0, format='%f')
tasa_interes = st.number_input('Tasa de interés anual (%)', min_value=0.0, max_value=100.0, format='%f') / 100
plazo_anios = st.number_input('Plazo del préstamo (años)', min_value=1, max_value=30, step=1)

# Cálculo de la cuota mensual
n_cuotas = plazo_anios * 12
tasa_mensual = tasa_interes / 12
if tasa_interes > 0:
    cuota_mensual = monto_prestamo * (tasa_mensual * (1 + tasa_mensual)**n_cuotas) / ((1 + tasa_mensual)**n_cuotas - 1)
else:
    cuota_mensual = monto_prestamo / n_cuotas

# Mostrar resultado del simulador de préstamos
st.write('Cuota mensual: Q', cuota_mensual)

# Sección para agregar futuras funcionalidades
st.header('Más funcionalidades próximamente')
st.write('Esta aplicación puede expandirse con más funcionalidades contables, como integración con la SAT, generación de reportes financieros, etc.')
