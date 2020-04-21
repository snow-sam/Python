import socket
import os
import json
import cv2
import numpy as np

def add_dic(dicionario):
        dicionario[input('Chave: ')] = [input('Nome: '), input('Idade: '), input('Cor: ')]

def del_dic(dicionario, chave):
    del dicionario[chave]
    print('Excluido')

def exibir_dic(dicionario):
    for chave, data in dicionario.items():
        print('Nome... '+ data[0])
        print('Idade... '+ data[1])
        print('Cor... '+ data[2])

def search_dic(dicionario, chave):
    for chave, dado in dicionario[chave]:
        print('Nome... '+ dado[0])
        print('Idade... '+ dado[1])
        print('Cor... '+ dado[2])

def keys_dic(dicionario):
    print (dicionario.keys())

def data_dic(dicionario,chave,dado):
    print(dicionario[chave][dado])


def alldata_dic(dicionario,dado):
    for key in dicionario.keys():
        print(dicionario[key][dado])

def changedata_dic(dicionario,chave,dado):
    newitem = input('Digite o novo item: ')
    dicionario[chave][dado] = newitem

def ler_arquivo(arquivo):
    if os.path.exists(arquivo):
        with open (arquivo , 'r') as arq_json:
            dicionario = json.load(arq_json)
    else:
            dicionario = {}
    return dicionario

def upload_dic(dicionario,arquivo):
    with open(arquivo ,'a') as arq_json:
        json.dump(dicionario, arq_json)

def registrar(dicionario,arquivo):
    n = input('Quantas Chaves? ')
    while len(dicionario.keys()) < n:
        add_dic(dicionario)
    upload_dic(dicionario,arquivo)

def exibir(arquivo):
    dicionario = ler_arquivo(arquivo)
    exibir_dic(dicionario)





def order_points(pts):
	# initialzie a list of coordinates that will be ordered
	# such that the first entry in the list is the top-left,
	# the second entry is the top-right, the third is the
	# bottom-right, and the fourth is the bottom-left
	rect = np.zeros((4, 2), dtype = "float32")
	# the top-left point will have the smallest sum, whereas
	# the bottom-right point will have the largest sum
	s = pts.sum(axis = 1)
	rect[0] = pts[np.argmin(s)]
	rect[2] = pts[np.argmax(s)]
	# now, compute the difference between the points, the
	# top-right point will have the smallest difference,
	# whereas the bottom-left will have the largest difference
	diff = np.diff(pts, axis = 1)
	rect[1] = pts[np.argmin(diff)]
	rect[3] = pts[np.argmax(diff)]
	# return the ordered coordinates
	return rect



def four_point_transform(image, pts):
	# obtain a consistent order of the points and unpack them
	# individually
	rect = order_points(pts)
	(tl, tr, br, bl) = rect
	# compute the width of the new image, which will be the
	# maximum distance between bottom-right and bottom-left
	# x-coordiates or the top-right and top-left x-coordinates
	widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
	widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
	maxWidth = max(int(widthA), int(widthB))
	# compute the height of the new image, which will be the
	# maximum distance between the top-right and bottom-right
	# y-coordinates or the top-left and bottom-left y-coordinates
	heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
	heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
	maxHeight = max(int(heightA), int(heightB))
	# now that we have the dimensions of the new image, construct
	# the set of destination points to obtain a "birds eye view",
	# (i.e. top-down view) of the image, again specifying points
	# in the top-left, top-right, bottom-right, and bottom-left
	# order
	dst = np.array([
		[0, 0],
		[maxWidth - 1, 0],
		[maxWidth - 1, maxHeight - 1],
		[0, maxHeight - 1]], dtype = "float32")
	# compute the perspective transform matrix and then apply it
	M = cv2.getPerspectiveTransform(rect, dst)
	warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
	# return the warped image
	return warped