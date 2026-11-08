class Solution(object):
    def numUniqueEmails(self, emails):
        temp = []
        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.' , '')
            if '+' in local:
                local = local[:local.index('+')]
            
            email_rec = local + '@' + domain
            
            if email_rec not in temp:
                temp.append(email_rec)    
        
        return len(temp)