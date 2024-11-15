import reflex as rx

def index() -> rx.Component:
    return rx.container(

        rx.heading("PELICULAS-YA",
        color="red",
        size="6",
        padding="20px",
        hight="100vh",
        width="100%",
        position="absolute",
        top="0",
        left="0"
        ),
        rx.link(
             rx.button("iniciar secion",bg="red",href="https://forms.gle/rptSMjFmtEQqKEMW9"),position="absolute",
        top="20px",
        right="20px",
        z_index=10
        ),
        rx.box(
             rx.button("registrate   ",bg="red"),position="absolute",
        top="20px",
        right="150px",
        z_index=10
        ),
        rx.hstack(
            rx.text(
                "PELICULAS-YA ",
                size="5", color="white"
            ),
            rx.text(
                "Food Puquio es una aplicación móvil diseñada para conectar a los amantes de la comida con una amplia gama de restaurantes y opciones culinarias. Su nombre, Food Puquio, evoca la imagen de un manantial de sabores, haciendo referencia a la abundancia y variedad de opciones que ofrece la aplicación",
                size="5",
            ),
            rx.vstack(
                rx.hstack(
                    rx.link(
                        rx.button("Registrate aqui!",color_scheme="green"),
                        href="https://forms.gle/Gj2CstmbZuhy1V2c9",
                        is_external=True,
                    ),
                    
                ),
                
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),

        height="100vh",
        width="100%",
        background="url('https://www.teknofilo.com/wp-content/uploads/2021/06/Netflix-1280x720.jpg')",
        background_size="cover",
        background_position="center"
    ),


app = rx.App()
app.add_page(index)