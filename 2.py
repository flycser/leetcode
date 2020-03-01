#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-27 22:26:02
# @Author  : Fei Jie (hfut_jf@aliyun.com)
# @Link    : https://flycser.github.io
# @Version : $Id$

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def addTwoNumbers(self, l1, l2):
		carry_bit = 0
		cur_bit = 0
		prev_node = ListNode(0)
		start_node = prev_node
		cur_node_1 = l1
		cur_node_2 = l2
		while True:
			if cur_node_1 and cur_node_2:
				prev_node.next = ListNode(0)
				val = cur_node_1.val + cur_node_2.val + carry_bit
				cur_bit = val % 10
				carry_bit = val // 10
				# print(cur_node_1.val, cur_node_2.val, cur_bit, carry_bit)

				prev_node.next.val = cur_bit
				prev_node = prev_node.next

				# print_linked_list(start_node)
			else:
				break

			cur_node_1 = cur_node_1.next
			cur_node_2 = cur_node_2.next

		if cur_node_1 is None and cur_node_2 is None and carry_bit < 1:
			# print_linked_list(start_node)
			pass
		elif cur_node_1:
			while True:
				val = cur_node_1.val + carry_bit
				cur_bit = val % 10
				carry_bit = val // 10

				prev_node.next = ListNode(0)
				prev_node.next.val = cur_bit
				prev_node = prev_node.next

				cur_node_1 = cur_node_1.next
				if cur_node_1 is None:
					break
		elif cur_node_2:
			while True:
				val = cur_node_2.val + carry_bit
				cur_bit = val % 10
				carry_bit = val // 10

				prev_node.next = ListNode(0)
				prev_node.next.val = cur_bit
				prev_node = prev_node.next

				cur_node_2 = cur_node_2.next
				if cur_node_2 is None:
					break
		if carry_bit > 0:
			prev_node.next = ListNode(0)
			prev_node.next.val = carry_bit
			prev_node = prev_node.next

		return start_node.next


def print_linked_list(l1):

	while True:
		print(l1.val, end=' ')
		l1 = l1.next
		if l1 is None:
			break
	print()


if __name__ == '__main__':
	
	l1 = ListNode(2)
	l1.next = ListNode(4)
	l1.next.next = ListNode(3)
	# l1.next.next.next = ListNode(5)
	# l1 = ListNode(5)
	# l1.next = ListNode(9)
	# l1.next.next = ListNode(8)
	# l1.next.next.next = ListNode(9)

	# l2 = ListNode(5)
	l2 = ListNode(5)
	l2.next = ListNode(6)
	l2.next.next = ListNode(4)

	solution = Solution()
	l3 = solution.addTwoNumbers(l1, l2)

	print_linked_list(l3)