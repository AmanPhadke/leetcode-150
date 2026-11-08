class Solution(object):
    def numUniqueEmails(self, emails):
        temp = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.' , '')
            if '+' in local:
                local = local[:local.index('+')]
            
            email_rec = local + '@' + domain
            
            temp.add(email_rec)

        
        return len(temp)