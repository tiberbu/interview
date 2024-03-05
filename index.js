function maskDatesAndEmails(inputString) {
    const datePattern = /\b(\d{2}\/\d{2}\/\d{2})\b/g; 
    const emailPattern = /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b/g;

    const dateMask = '**/**/***'; 
    const emailMask = '*****@*****.***'; 

    const maskedString = inputString
        .replace(datePattern, dateMask)
        .replace(emailPattern, emailMask);

    return maskedString;
}



