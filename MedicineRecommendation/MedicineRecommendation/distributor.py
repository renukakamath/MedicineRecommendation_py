from public import *


distributor=Blueprint('distributor',__name__)

@distributor.route('/distributor_home')
def distributor_home():
	if not session.get('lid') is None:
		return render_template('distributor_home.html')
	else:
		return redirect(url_for('public.login'))


@distributor.route('/dis_view_medicine',methods=['get','post'])
def dis_view_medicine():
	if not session.get('lid') is None:
		data={}
		# q="select * from medicine "
		# res=select(q)
		with open(compiled_contract_path) as file:
			contract_json = json.load(file)  # load contract info as JSON
			contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
		contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
		blocknumber = web3.eth.get_block_number()
		res = []
		try:
			for i in range(blocknumber, 0, -1):
				a = web3.eth.get_transaction_by_block(i, 0)
				decoded_input = contract.decode_function_input(a['input'])
				print(decoded_input)
				# if str(decoded_input[0]) == "<Function add_medicine(uint256,uint256,string,string,string,string,string,string,string,string)>":
				# 		res.append(decoded_input[1])

				if str(decoded_input[0]) == "<Function add_medicine(uint256,uint256,uint256,string,string,string,string,string,string,string,string,string)>":
					# if int(decoded_input[1]['m_id']) == int(session['lid'])  :
						res.append(decoded_input[1])
		except Exception as e:
			print("", e)

		data['medsssiiiii']=res
		print("llllllllllllllllllllllllllllllllllllllllllll",res)






		# with open(compiled_contract_path) as file:
		# 	contract_json = json.load(file)  # load contract info as JSON
		# 	contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
		# contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
		# blocknumber = web3.eth.get_block_number()
		# res = []
		# try:
		# 	for i in range(blocknumber, 0, -1):
		# 		a = web3.eth.get_transaction_by_block(i, 0)
		# 		decoded_input = contract.decode_function_input(a['input'])
		# 		print("jjjjjjjjjjj",decoded_input)
		# 		if str(decoded_input[0]) == "<Function add_medicine(uint256,uint256,string,string,string,string,string,string,string,string)>":
		# 				res.append(decoded_input[1])
		# except Exception as e:
		# 	print("", e)

		# data['medinnnnn']=res
		# print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkk",res)

		
		
		return render_template('dis_view_medicine.html',data=data)
	else:
		return redirect(url_for('public.login'))



@distributor.route('/distributor_view_stock',methods=['get','post'])
def distributor_view_stock():
	if not session.get('lid') is None:
		data={}
		mid=request.args['mid']
		q="select * from stock where medicine_id='%s' "%(mid)
		data['med']=select(q)
		if 'action' in request.args:
			action=request.args['action']
			s_id=request.args['s_id']
			mid=request.args['mid']
		else:
			action=None
			
		if action=="buy":
			q="select"
			
			q="update stock set distributer_id='%s' where stock_id='%s'"%(session['lid'],s_id)
			print(q)
			update(q)
			flash('picked successfuly')
			return redirect(url_for('distributor.dis_view_medicine',mid=mid))



		return render_template('distributor_view_stock.html',data=data)
	else:
		return redirect(url_for('public.login'))


@distributor.route('/distributor_view_manufacture',methods=['get','post'])
def distributor_view_manufacture():
	if not session.get('lid') is None:
		data={}
		m_id=request.args['m_id']
		q="select * from manufacture where login_id='%s' "%(m_id)
		data['med']=select(q)

		return render_template('distributor_view_manufacture.html',data=data)
	else:
		return redirect(url_for('public.login'))



@distributor.route('/distributor_view_medicine_request',methods=['get','post'])
def distributor_view_medicine_request():
	if not session.get('lid') is None:
		data={}
		lid=session['lid']
		mid=request.args['mid']
		m_id=request.args['m_id']
		data['m_id']=m_id
		if "req" in request.args:
			req=request.args['req']

			with open(compiled_contract_path) as file:
				contract_json = json.load(file)  # load contract info as JSON
				contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
				contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
				blocknumber = web3.eth.get_block_number()
				res = []
				try:
					for i in range(blocknumber, 0, -1):
						a = web3.eth.get_transaction_by_block(i, 0)
						decoded_input = contract.decode_function_input(a['input'])
						# print(decoded_input)
						if str(decoded_input[0]) == "<Function add_medicine(uint256,uint256,uint256,string,string,string,string,string,string,string,string)>":
								
								if int(decoded_input[1]['mid']) == int(mid):
									res.append(decoded_input[1]['m_id'])
								
								print("fhdfhfghfghfg",res)
				except Exception as e:
					print("", e)

			

			# q="update request set manufacture_id='%s',status='Send to Manufacture' where request_id='%s'"%(mid,req)
			# print(q)
			# update(q)


		if 'action' in request.args:
			print("_________________________________________________________________________")
			action=request.args['action']
			req=request.args['req']
			mid=request.args['mid']
			m_id=request.args['m_id']
			print(action)
			# data['m_id']=m_id
		else:
			action=None


		if action == "sendssss":

			# man=request.form['man']
			q="update request set manufacture_id='%s',status='Send to Manufacture' where request_id='%s'"%(m_id,req)
			print("???????????",q)
			update(q)
			return redirect(url_for('distributor.dis_view_medicine',mid=mid,m_id=m_id))

		q="SELECT * FROM request INNER JOIN pharmacy ON `pharmacy`.`login_id`=`request`.`pharmacy_id` where distributer_id='%s'and medicine_id='%s'"%(lid,mid)
		print(q)
		res=select(q)
		print(res)
		data['req']=res
		return render_template('distributor_view_medicine_request.html',data=data)
	else:
		return redirect(url_for('public.login'))



@distributor.route('/distributor_send_manufacturer',methods=['get','post'])
def distributor_send_manufacturer():
	if not session.get('lid') is None:
		data={}
		lid=session['lid']
		# mid=request.args['mid']


		if 'action' in request.args:
			print("_________________________________________________________________________")
			action=request.args['action']
			req=request.args['req']
			mid=request.args['mid']
			m_id=request.args['m_id']
			print(action)
			# data['m_id']=m_id
		else:
			action=None


		if action == "sendssss":

			# man=request.form['man']
			q="update request set manufacture_id='%s',status='Send to Manufacture' where request_id='%s'"%(m_id,req)
			print("???????????",q)
			update(q)
			return redirect(url_for('distributor.dis_view_medicine',mid=mid,m_id=m_id))

		# with open(compiled_contract_path) as file:
		# 	contract_json = json.load(file)  # load contract info as JSON
		# 	contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
		# contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
		# blocknumber = web3.eth.get_block_number()
		# res = []
		# try:
		# 	for i in range(blocknumber, 0, -1):
		# 		a = web3.eth.get_transaction_by_block(i, 0)
		# 		decoded_input = contract.decode_function_input(a['input'])
		# 		# print(decoded_input)
		# 		if str(decoded_input[0]) == "<Function add_medicine(uint256,uint256,string,string,string,string,string,string,string,string)>":
		# 				if int(decoded_input[1]['mid']) == int(mid):
		# 					res.append(decoded_input[1])
						
		# 				# 	print("fhdfhfghfghfg",res)
		# except Exception as e:
		# 	# print("", e)




		# q="select * from manufacture"
		# res=select(q)
		# data['man']=res



		return render_template('distributor_send_manufacturer.html',data=data)
	else:
		return redirect(url_for('public.login'))