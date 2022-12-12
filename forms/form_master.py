import tkinter as tk
from tkinter import ttk, messagebox, RIGHT, Y
from tkinter.font import BOLD

from tkcalendar import Calendar

from tkinter import ttk, CENTER, LEFT, X, TOP


class MasterPanel:

    def is_not_none(self):
        horas = self.combo2.get()
        ubicacion = self.combo.get()
        date = self.calendar_entry.get_date()
        if horas != "" and ubicacion != "" and date is not None:
            messagebox.showerror(message=f"Hora: {horas}, Ubicacion: {ubicacion}, Fecha: {date}", title="Mensaje")
        else:
            messagebox.showerror(message="Los datos estan nulos", title="Mensaje")

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Master panel')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)

        scrollbar = tk.Scrollbar(self.ventana)
        scrollbar.pack(side=RIGHT, fill=Y)


        # frame_form : FRAME GRANDE DE LA IZQUIERDA QUE AGRUPA EL FRAME DE LOS INPUTS Y FRAME DEL TITULO
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="left", expand=tk.YES, fill=tk.BOTH)
        # frame_form

        # frame_form_top : INCLUYE EL FRAME DEL TITULO
        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Ingrese los datos", font=('Times', 30), fg="#666a88", bg='#fcfcfc',
                         pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)
        # end frame_form_top

        # frame_form_fill FRAME QUE AGRUPA LOS INPUTS
        frame_form_fill = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        etiqueta_formato = tk.Label(frame_form_fill, text="Selecione el rango de las horas:", font=('Times', 14), fg="#666a88",
                                    bg='#fcfcfc',
                                    anchor="w")
        etiqueta_formato.pack(fill=tk.X, padx=20, pady=5)

        # COMBOBOX HORAS

        self.combo2 = ttk.Combobox(
            frame_form_fill,
            state="readonly",
            values=["7:00 AM - 10:00 AM", "10:00 AM - 1:00 PM", "1:00 PM - 4:00 PM", "4:00 PM - 7:00 PM",
                    "7:00 PM - 10:00 PM"],
            font=('Times', 14)
        )
        self.combo2.pack(fill=tk.X, padx=20, pady=10)

        """
        # HORA INICIAL
        
        initial_hour = tk.Label(frame_form_fill, text="Hora Inicial", font=('Times', 14), fg="#666a88", bg='#fcfcfc',
                                anchor="w")
        initial_hour.pack(fill=tk.X, padx=20, pady=5)
        self.first_hour = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.first_hour.pack(fill=tk.X, padx=20, pady=10)

        # HORA FINAL

        final_hour = tk.Label(frame_form_fill, text="Hora final", font=('Times', 14), fg="#666a88", bg='#fcfcfc',
                              anchor="w")
        final_hour.pack(fill=tk.X, padx=20, pady=5)
        self.second_hour = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.second_hour.pack(fill=tk.X, padx=20, pady=10)
        
        """

        etiqueta_calendario = tk.Label(frame_form_fill, text="Selecione la fecha a consultar:", font=('Times', 14),
                                    fg="#666a88",
                                    bg='#fcfcfc',
                                    anchor="w")
        etiqueta_calendario.pack(fill=tk.X, padx=20, pady=5)

        # CALENDARIO
        self.calendar_entry = Calendar(frame_form_fill, selectmode='day', year=2022, month=10, day=12)
        self.calendar_entry.pack(pady=20)

        def grad_date():
            date.config(text="La fecha que seleccionó es: " + self.calendar_entry.get_date())

        # Add Button and Label
        tk.Button(frame_form_fill, text="Revisar fecha",
                  command=grad_date).pack(fill=tk.X, padx=20, pady=10)

        date = tk.Label(frame_form_fill, text="")
        date.pack(fill=tk.X, padx=20, pady=10)

        etiqueta_ubicacion = tk.Label(frame_form_fill, text="Selecione la ubicación que desea revisar:", font=('Times', 14),
                                       fg="#666a88",
                                       bg='#fcfcfc',
                                       anchor="w")
        etiqueta_ubicacion.pack(fill=tk.X, padx=20, pady=5)

        # COMBOBOX UBICACION

        self.combo = ttk.Combobox(
            frame_form_fill,
            state="readonly",
            values=["UPTC", "NIEVES", "GREEN HILLS", "CONCESIONARIOS", "LUMOL", "HONGOS", "RETEN SUR"],
            font=('Times', 14)
        )
        self.combo.pack(fill=tk.X, padx=20, pady=10)

        button_result = tk.Button(frame_form_fill, text="Ver datos ingresados", font=('Times', 15, BOLD), bg='#3a7ff6', bd=0,
                           fg="#fff", command=self.is_not_none)
        button_result.pack(fill=tk.X, padx=20, pady=20)
        button_result.bind("<Return>", (lambda event: self.is_not_none()))


        # frame_title_result FRAME GRANDE DE LA DERECHA QUE AGRUPARA EL FRAME DEL TITULO Y EL FRAME CON RESULTADOS
        frame_result = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#fcfcfc')
        frame_result.pack(side="right", expand=tk.YES, fill=tk.BOTH)

        # frame_title_result
        frame_title_result = tk.Frame(frame_result, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_title_result.pack(side="top", fill=tk.X)
        title = tk.Label(frame_title_result, text="Resultados obtenidos", font=('Times', 30), fg="#666a88", bg='#fcfcfc',
                         pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)
        # end frame_form_top


        self.ventana.mainloop()
