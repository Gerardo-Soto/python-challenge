		temp = l1
		temp2 = l2
		prev = temp
		while temp and temp2:
			if temp.val>temp2.val:
				if prev == l1:
					if prev.val < temp2.val:
						a = temp2
						temp2 = temp2.next
						a.next = temp
						prev.next = a
						prev = prev.next
						continue
					l1 = temp2
					a = temp2
					temp2 = temp2.next
					a.next = prev
					temp = prev = l1
					
				else:
					prev.next = temp2
					a = temp2
					temp2 = temp2.next
					a.next = temp
					prev = prev.next
					continue
			prev = temp
			temp = temp.next
			
		if temp == None and temp2!=None:
			if l1 == None:
				return l2
			prev.next = temp2
	return l1