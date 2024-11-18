import reflex as rx

def index() -> rx.Component:
    return rx.container(

        rx.heading("PELICULAS YA",
        font_family="Netflix, sans-serif",
        color="red",
        size="50",
        padding="35px",
        hight="100vh",
        width="100%",
        position="absolute",
        top="0",
        left="0",
        text_shadow="2px 2px 4px black, -2px -2px 4px black, 2px -2px 4px black, -2px 2px 4px black" ,
        font_size="28px",
        weight="bold"

        ),
        rx.link(
             rx.button("iniciar secion",bg="black"),
             href="https://forms.gle/rptSMjFmtEQqKEMW9",
        position="absolute",
        top="20px",
        right="20px",
        z_index=10,
        color="black"
        ),
        rx.link(
             rx.button("vista previa",bg="red"),position="absolute",
        top="20px",
        right="150px",
        z_index=10
        ),
        rx.vstack(
            rx.heading("TODAS LAS PELICULAS, SERIES QUE DESEAS VER",
                       text_shadow="2px 2px 4px black, -2px -2px 4px black, 2px -2px 4px black, -2px 2px 4px black",
                       font_size="48px",
                       size="9",
                       align="center"
                       ),
            rx.text("disfruta donde quieras, cancela solo porla pelicula que quieras",
                padding="10px",  # Un poco de espacio alrededor del texto  
                color="white",  # Color del texto
                font_size="18px",  # Tamaño de la fuente
                text_shadow="2px 2px 4px black, -2px -2px 4px black, 2px -2px 4px black, -2px 2px 4px black"  # Borde negro simulado
                ),
            rx.text("¿quieres ver algo yaa? Inicia secion y opten una subcripcion gratis por 1 mes",
                    font_size="14px",
                    color="white",
                    text_shadow="2px 2px 4px black, -2px -2px 4px black, 2px -2px 4px black, -2px 2px 4px black"
                    ),
            rx.hstack(
                rx.input(
                name="input",
                placeholder="Nombre de tu pelicula",
                type="text",
                required=True,
                 style={"width":"400px", 
                        "height": "40px", 
                        "fontSize": "20px",
                        "backgroundColor": "black",
                        "color": "black"} 
                
            ),
            rx.button("EMPEZAR",
                type="submit",
                height="40px",
                font_size="15px",
                width="150px",
                bg="red",
                ),
                border_shadow="2px 2px 4px black, -2px -2px 4px black, 2px -2px 4px black, -2px 2px 4px black",
                gap="0",
            
            ),
            justify="center",
            align="center",
            position="absolute",
            top="50%",          # Centrado vertical al 50% de la altura
            left="50%",         # Centrado horizontal al 50% del ancho
            transform="translate(-50%, -50%)",  # Corrección de la posición para centrar completamente
            size="cover"
           
        ),
        height="100vh",
        width="100%",
        background="url('https://www.teknofilo.com/wp-content/uploads/2021/06/Netflix-1280x720.jpg')",
        background_size="cover",
        background_position="center"
    ),


app = rx.App()
app.add_page(index)