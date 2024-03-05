function maskSensitiveData(jsonData) {
  
    const maskedData = {...jsonData}; // Create a copy of jsonData

    // Mask email
    if (maskedData.email)
        maskedData.email = "*****" + maskedData.email.substring(5); // Keep characters from index 5 onwards

    // Mask first name
    if (maskedData.first_name && maskedData.first_name.length > 2)
        maskedData.first_name = "**" + maskedData.first_name.substring(2); // Keep characters from index 2 onwards

    // Mask date of birth
    if (maskedData.date_of_birth && maskedData.date_of_birth.length > 2)
        maskedData.date_of_birth = "**" + maskedData.date_of_birth.substring(2); // Keep characters from index 2 onwards

    return maskedData;
}

// Example usage:


const maskedData = maskSensitiveData(jsonData);
console.log(maskedData);

