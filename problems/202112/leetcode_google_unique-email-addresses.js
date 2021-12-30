/**
 * @param {string[]} emails
 * @return {number}
 */
var numUniqueEmails = function(emails) {
  const emailSet = new Set();
  emails.forEach((email) => {
      const [localName, domainName] = email.split('@')
      let processedLocalName = ''
      for (let i =0;i<localName.length;i++) {
          if (localName[i] === '+') break
          if (localName[i] === '.') continue
          processedLocalName += localName[i]
      }
      emailSet.add(processedLocalName + '@' + domainName)
  })
 return emailSet.size
};