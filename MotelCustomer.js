alert('Motel Customer QAP 4'); 
console.log ('Motel Customer QAP 4') 


// Object Literals
const person = {
    name: 'Lianne Campbell',
    birthdate: '11/17/1992',
    gender: 'Female',
    room_preferences: ['Smoking,King Bed,Bathtub,Wi-Fi'],
    payment_method: 'Visa',
    mailing_address: {
        street: '434 Thorburn Road.',
        city: 'St. Johns',
        province: 'NL',
        postal: 'A1B4R1',
        country: 'CANADA'
    },
    phone_number: '(709)754-5430',
    check_in: '11/23/2023',
    check_out: {
        time: '12:00PM',
        date: '11/25/2023',
    },
 
// Functions

    getAge: function() {
        const today = new Date();
        const birthdate = new Date(this.birthdate);
        const person_age = today.getFullYear() - birthdate.getFullYear();
    
// Adjust age if the birthday hasn't occurred yet this year
        if (today.getMonth() < birthdate.getMonth() || (today.getMonth() === birthdate.getMonth() && today.getDate() < birthdate.getDate())) {
            return person_age - 1;
        }
    
        return person_age;
    },

    getStay: function(){
        const checkInDate = new Date(this.check_in);
        const checkOutDate = new Date(this.check_out.date);
        const durationInMilliseconds = checkOutDate - checkInDate;
        const durationInDays = durationInMilliseconds / (1000 * 60 * 60 * 24);
        return durationInDays;
    },
}


console.log(person)

  let age;
  age = person.getAge();
  console.log(age)

  let staytime; 
  staytime = person.getStay();
  console.log(staytime)

