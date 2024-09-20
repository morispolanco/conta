import streamlit as st
import pandas as pd
import datetime

# Título de la aplicación
st.title('Suite Contable para Guatemala')

# Menú lateral para seleccionar la aplicación
opcion = st.sidebar.selectbox(
    'Selecciona una Aplicación',
    ('Cálculo de Impuestos', 
     'Facturación Electrónica (FEL)', 
     'Gestión de Nóminas', 
     'Análisis Financiero', 
     'Recordatorios Fiscales')
)

# Función para cálculo de impuestos (IVA e ISR)
def calculo_impuestos():
    st.header('Cálculo de IVA e ISR')
    
    # Cálculo de IVA
    st.subheader('Cálculo de IVA')
    iva_rate = 0.12
    ventas_brutas = st.number_input('Ventas Brutas (sin IVA)', min_value=0.0, format='%f')
    compras_brutas = st.number_input('Compras Brutas (sin IVA)', min_value=0.0, format='%f')

    iva_ventas = ventas_brutas * iva_rate
    iva_compras = compras_brutas * iva_rate
    iva_a_pagar = iva_ventas - iva_compras

    st.write('IVA sobre Ventas: Q', iva_ventas)
    st.write('IVA sobre Compras: Q', iva_compras)
    st.write('IVA a pagar: Q', iva_a_pagar)

    # Cálculo de ISR
    st.subheader('Cálculo de ISR')
    ingresos = st.number_input('Ingrese sus ingresos anuales', min_value=0.0, format='%f')
    deducciones = st.number_input('Ingrese sus deducciones permitidas', min_value=0.0, format='%f')
    base_imponible = ingresos - deducciones

    if base_imponible <= 30000:
        isr = base_imponible * 0.05
    elif base_imponible <= 60000:
        isr = 1500 + (base_imponible - 30000) * 0.10
    else:
        isr = 4500 + (base_imponible - 60000) * 0.15

    st.write('Base imponible: Q', base_imponible)
    st.write('ISR a pagar: Q', isr)

# Función para facturación electrónica (simulada)
def facturacion_electronica():
    st.header('Facturación Electrónica (FEL)')
    
    cliente = st.text_input('Nombre del Cliente')
    nit = st.text_input('NIT del Cliente')
    producto = st.text_input('Producto o Servicio')
    precio = st.number_input('Precio del Producto/Servicio', min_value=0.0)
    cantidad = st.number_input('Cantidad', min_value=1)

    total = precio * cantidad
    st.write(f'Total a facturar: Q {total}')

    # Simulación de emisión de factura
    if st.button('Emitir Factura Electrónica'):
        st.write('Factura emitida para el cliente:', cliente)
        st.write('NIT:', nit)
        st.write(f'Total facturado: Q {total}')

# Función para gestión de nóminas
def gestion_nominas():
    st.header('Gestión de Nóminas')

    # Entrada de datos
    nombre_empleado = st.text_input('Nombre del Empleado')
    salario_base = st.number_input('Salario Base (Q)', min_value=0.0)
    igss = salario_base * 0.0483
    irtra = salario_base * 0.01
    bonificacion = 250.0  # Bonificación incentivo

    # Cálculo de salario neto
    salario_neto = salario_base + bonificacion - igss - irtra

    # Mostrar resultados
    st.write(f'Salario Neto: Q {salario_neto}')

    # Generación de informe en CSV
    if st.button('Generar Reporte de Nómina'):
        df = pd.DataFrame({
            'Empleado': [nombre_empleado],
            'Salario Base': [salario_base],
            'Bonificación': [bonificacion],
            'IGSS': [igss],
            'IRTRA': [irtra],
            'Salario Neto': [salario_neto]
        })
        df.to_csv('nomina.csv', index=False)
        st.write('Reporte generado con éxito.')

# Función para análisis financiero
def analisis_financiero():
    st.header('Análisis Financiero')

    # Proyección de Flujo de Caja
    st.subheader('Proyección de Flujo de Caja')
    ingresos = st.number_input('Ingresos Totales', min_value=0.0)
    egresos = st.number_input('Egresos Totales', min_value=0.0)
    flujo_neto = ingresos - egresos

    st.write(f'Flujo de Caja Neto: Q {flujo_neto}')

    # Proyección de escenarios
    st.subheader('Proyección de Escenarios a 3 Años')
    crecimiento = st.slider('Tasa de Crecimiento Anual (%)', min_value=0, max_value=20) / 100
    proyeccion_1 = flujo_neto * (1 + crecimiento)
    proyeccion_2 = proyeccion_1 * (1 + crecimiento)
    proyeccion_3 = proyeccion_2 * (1 + crecimiento)

    st.write(f'Flujo proyectado para el año 1: Q {proyeccion_1}')
    st.write(f'Flujo proyectado para el año 2: Q {proyeccion_2}')
    st.write(f'Flujo proyectado para el año 3: Q {proyeccion_3}')

# Función para recordatorios fiscales
def recordatorios_fiscales():
    st.header('Recordatorios Fiscales')

    # Selección de fechas importantes
    fecha_iva = st.date_input('Fecha límite para presentación de IVA', datetime.date.today())
    fecha_isr = st.date_input('Fecha límite para presentación de ISR', datetime.date.today())

    # Mostrar recordatorios
    st.write(f'Fecha límite para IVA: {fecha_iva}')
    st.write(f'Fecha límite para ISR: {fecha_isr}')

    # Simulación de recordatorio
    if st.button('Configurar Recordatorio'):
        st.write('Recordatorios configurados para IVA e ISR.')

# Ejecutar la funcionalidad seleccionada en el menú
if opcion == 'Cálculo de Impuestos':
    calculo_impuestos()
elif opcion == 'Facturación Electrónica (FEL)':
    facturacion_electronica()
elif opcion == 'Gestión de Nóminas':
    gestion_nominas()
elif opcion == 'Análisis Financiero':
    analisis_financiero()
elif opcion == 'Recordatorios Fiscales':
    recordatorios_fiscales()
