export const validateEmployee = (formData) => {
  const errors = {};
  
  if (!formData.get('first_name')) {
    errors.first_name = 'First name is required';
  }
  
  if (!formData.get('last_name')) {
    errors.last_name = 'Last name is required';
  }
  
  if (!formData.get('email') || !/\S+@\S+\.\S+/.test(formData.get('email'))) {
    errors.email = 'Valid email is required';
  }
  
  if (!formData.get('date_of_birth')) {
    errors.date_of_birth = 'Date of birth is required';
  } else {
    const age = calculateAge(new Date(formData.get('date_of_birth')));
    if (age < 18) {
      errors.date_of_birth = 'Employee must be at least 18 years old';
    }
  }
  
  if (!formData.get('salary') || formData.get('salary') < 15000) {
    errors.salary = 'Salary must be at least $15,000';
  }

  return errors;
};

const calculateAge = (birthDate) => {
  const today = new Date();
  let age = today.getFullYear() - birthDate.getFullYear();
  const monthDiff = today.getMonth() - birthDate.getMonth();
  
  if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
    age--;
  }
  
  return age;
}; 