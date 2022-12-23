from kivy.lang import Builder
from kivymd.uix.scrollview import MDScrollView
from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.pickers import MDDatePicker
from kivymd.app import MDApp
from kivy.core.window import Window
import json

KV = '''


MDScreenManager:

    MDScreen:
        name: "main"
        MDGridLayout:
            cols: 1
            MDRaisedButton:
                font_size: "32sp"
                text: "Enter payments"
                pos_hint: {"y": .2, "center_x" : .5}
                size_hint: 1, 1
                on_release:
                    root.current = "enter"
            MDRaisedButton:
                font_size: "32sp"
                text: "Check payments"
                pos_hint: {"y": .6, "center_x" : .5}
                size_hint: 1, 1
                on_release:
                    root.current = "view"
           
        
    MDScreen:
    #----------------------------------------------------------------------------------------------------------------------
        name: "enter"
        ScrollView:
            do_scroll_x: False
            do_scroll_y: True
            bar_width: 10
            always_overscroll: False
            
            MDFloatLayout:
                size_hint_y: None
                always_overscroll: False
                
                size: root.width, root.height*1.01   
                MDLabel:
                    text: "Date"
                    pos_hint: {"x" : 0, "center_y" : .9}
                    size_hint: None, None
                MDIconButton:
                    icon: "calendar"  
                    pos_hint: {"center_x": .3, "center_y": .9}
                    on_release: app.show_date_picker()
                MDTextField:
                    id: date 
                    helper_text: "Enter a valid date yyyy/mm/dd "
                    date_format: 'yyyy/mm/dd'
                    validator: "date"
                    hint_text: "Enter date"
                    pos_hint: {"center_x" : 0.9, "center_y" : .9}
                    text: ""  
                MDLabel:
                    text: "Case id"              
                    pos_hint: {"x": 0, "center_y": .8}
                MDTextField:
                    id: case_id
                    hint_text: "Enter case id"
                    pos_hint: {"center_x": .9, "center_y": .8}
                MDLabel:
                    text: "Payment type"
                    size_hint: 1, None
                    pos_hint: {"x": 0, "center_y": .7}
                MDTextField:
                    id: payment_type
                    hint_text: "Payment type"
                    pos_hint: {"center_x": .9, "center_y": .7}
                MDLabel:
                    text: "Amount"
                    pos_hint: {"x" : 0, "center_y": .6}
                MDSwitch:
                    pos_hint: {"center_x" : 0.3, "center_y" : 0.6}
                    on_active: app.on_checkbox_active(*args)
                MDTextField:
                    id: amount
                    hint_text: "Enter amount"
                    pos_hint: {"center_x": .9, "center_y": .6}
                MDTextField:
                    id: comp_fees
                    hint_text: "Compliance fees"
                    helper_text: "Only use when calculating part payment "
                    helper_text_mode: "persistent"
                    pos_hint: {"center_x": .9, "center_y": .5}
                MDLabel:
                    text: "Compliance fees"
                    pos_hint: {"x" : 0, "center_y": .5}
                MDTextField:
                    id: full_amount
                    hint_text: "Full amount"
                    helper_text: "Only use when calculating part payment "
                    helper_text_mode: "persistent"
                    pos_hint: {"center_x": .9, "center_y": .4}
                MDLabel:
                    text: "Full amount"
                    pos_hint: {"x" : 0, "center_y": .4}
                
                MDRaisedButton:
                    text: "Submit"
                    pos_hint: {"y": .2, "center_x" : .5}
                    size_hint: 1, 0.09
                    on_release: app.add_payment()
                MDRaisedButton:
                    text: "Calculate"
                    pos_hint: {"y": .105, "center_x" : .5}
                    size_hint: 1, 0.09
                    on_release: 
                        app.part_payment()
                   
                MDRaisedButton:
                    text: "Go back"
                    pos_hint: {"y": 0.01, "center_x" : .5}
                    size_hint: 1, 0.09
                    on_release:
                        root.current = "main"  
    #---------------------------------------------------------------------------------------------------------------      
            
        

    MDScreen:
        name: "view"
        MDGridLayout:
            cols: 1
            
            MDGridLayout:

                padding: 10, 10
                cols: 3
                ScrollView:
                    do_scroll_x: False
                    do_scroll_y: True
                    bar_width: 10
                    size_hint: 1, 1
                    always_overscroll: False

                    MDLabel:
                        id: print_date
                        text: "Nothing to display"
                        size_hint_y: None
                        height: self.texture_size[1]
                        text_size: self.width, None
                        
                MDTextField:
                    id: show_date
                    mode: "rectangle"
                    
                   

                MDIconButton:
                    icon: "calendar"    
                    
                    on_release: app.show_date_picker_1()

                
                    
                    
            MDRaisedButton:
                text: "Check payments"
                pos_hint: {"y" : .2}
                size_hint: 1, 0.2
                on_release:
                    app.view_payment()
            MDRaisedButton:
                text: "Total"
                pos_hint: {"y" : .1}
                size_hint: 1, 0.2
                on_release:
                    app.total()


            MDRaisedButton:
                text: "Go back"
                pos_hint: {"y" : 0}
                size_hint: 1, 0.2
                on_release:
                    root.current = "main"
            
    
'''
payments = {}
file = "work.json"

class Test(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def on_save(self, instance, value, date_range):
        '''sets the date in Add payment'''
        self.root.ids.date.text = str(value.strftime("%Y/%m/%d"))
        print(value)
    def on_save_1(self, instance, value, date_range):
        '''sets the date in view payment'''
        self.root.ids.show_date.text = str(value.strftime("%Y/%m/%d"))

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''

    def show_date_picker(self):
        '''calls the date picker in add payment window'''
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()
        
    def show_date_picker_1(self):
        '''calls the date picker in view window'''
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save_1, on_cancel=self.on_cancel)
        date_dialog.open()
        
        
    
    def on_checkbox_active(self, checkbox, value):
        
        if value:
            payment_amount = float(self.root.ids.amount.text) * 1.5
        else: 
            payment_amount = float(self.root.ids.amount.text) / 1.5

        self.root.ids.amount.text = str(payment_amount)
        ##########################################
    def add_payment(self):
        """creates dictionary entry and saves it."""
        
        # sets date as user input in date field
        date = self.root.ids.date.text 
        # sets case_id as user input in case_id field
        case_id = self.root.ids.case_id.text
        # sets amount as user input in amount field
        amount = self.root.ids.amount.text
        # sets payment_type as user input in payment_type field
        payment_type = self.root.ids.payment_type.text
        try:
            self._extracted_from_add_payment_11(date, case_id, payment_type, amount)
        except ValueError as Error:
            self._extracted_from_add_payment_11(date, case_id, payment_type, amount)

    # TODO Rename this here and in `add_payment`
    def _extracted_from_add_payment_11(self, date, case_id, payment_type, amount):
        # checks if json file exists if it doesnt creates it if it does it dumps payments in it
        try:
            with open(file, 'x') as f:
                payments = {}
                j = json.dump(payments, f)
        except FileExistsError:
            with open(file, 'r') as f:
                payments = json.load(f)               
            
        #creates entry in dictionary if date exists appends it if not creates an entry
        if date not in payments:
            payments[date] = []
        payments[date].append(
            {
                "Case id" : case_id,
                "Payment type" : payment_type,
                "Amount" : amount
            })
        #resets the input fields to empty
        self.root.ids.case_id.text = ''
        self.root.ids.amount.text = ''
        self.root.ids.payment_type.text = ''
        #dumps data in json
        with open(file, 'w') as f:
            j = json.dump(payments, f)   
            
    def part_payment(self):
        """calculates part payment fees"""
        
        enf_fee = 235
        comp_fee = 75
        full_comp_fee = comp_fee * int(self.root.ids.comp_fees.text)
        full_amount = int(self.root.ids.full_amount.text)
        payed = int(self.root.ids.amount.text)


        x = (enf_fee / (full_amount - full_comp_fee) * (payed - full_comp_fee)) + full_comp_fee / 2
        self.root.ids.comp_fees.text = ""
        self.root.ids.full_amount.text = ""
        self.root.ids.amount.text = f"{x:.2f}"
            
    def view_payment(self):
        """finds entry in dictionary and puts all matches to a label"""
        
        #sets date as input from date field
        date = self.root.ids.show_date.text
        #sets print_date label to empty
        self.root.ids.print_date.text = ""
        #loads data from json
        with open(file, 'r') as f:
            payments = json.load(f)
            #if it finds entry puts it in a label if not sets label text as date does not exist
            try:
                for b, i in enumerate(payments.get(date, None), start=0):
                    self.root.ids.print_date.text += f"{b+1}. Case id:{payments[date][b].get('Case id')}, Payment type:{payments[date][b].get('Payment type')}, Amount:{payments[date][b].get('Amount')}.\n" 
            except (KeyError, TypeError) as error: # handle file not found on first launch
                date = self.root.ids.show_date.text
                self.root.ids.print_date.text = "No payments or wrong date"
                
    def total(self):
        """finds entrys in specific date and sums them up"""
        
        #sets date as input from show_date field
        date = self.root.ids.show_date.text
        #resets print_date label to empty
        self.root.ids.print_date.text = ''
        total1 = 0
        # finds required dates amount entrys and sums them
        try:
            with open(file, 'r') as f:
                payments = json.load(f)
                for i in payments[date]:
                    # if there is no value it skips it and look for other entry 
                    if amount := i.get('Amount'):
                        total1 += float(amount)
                self.root.ids.print_date.text += str(total1)
        except (KeyError,ValueError) as Error:
            self.root.ids.print_date.text = 'Date does not exist'


Test().run()

