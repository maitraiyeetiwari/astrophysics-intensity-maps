#ipython --pylab

import aplpy
import matplotlib.pyplot as mpl

fig = mpl.figure(figsize=(10,10))
#f1 = aplpy.FITSFigure('rcw49_cii_gusto.fits',north=True,figure =fig,subplot=[0,0.1,0.35,0.8])


f1 =aplpy.FITSFigure('ngc1977_cii_model_mom_0.fits',north=True,figure =fig, subplot=[0,0.1,0.35,0.8])

f1.tick_labels.set_font(size=10)
f1.axis_labels.set_font(size=10)
f1.axis_labels.set_ytext('Dec. (J2000)')
f1.axis_labels.set_xtext('R.A. (J2000)')
f1.show_colorscale(vmin=0,cmap='jet')

f1.add_colorbar(pad=0.3,location='right', axis_label_text="K kms$^{-1}$")
f1.colorbar.set_font(size=10)
f1.add_label(0.23, 0.9, 'NGC 1977', relative=True, size=15,color='orangered')
#f1.add_label(0.32, 0.85, '2 to 8 kms$^{-1}$', relative=True, size=15,color='white')
#f2.add_label(0.85, 0.95, 'CII @15"', relative=True, size=15,color='red')
#f1.show_contour('co_tdv_16_22.fits', colors='gray')

f1.set_xaxis_coord_type('scalar')
f1.set_yaxis_coord_type('scalar')


f1.recenter(83.865,-4.74, width=0.64,height=0.56)
#f1.show_contour('rcw49_cii_original.fits',levels=[70,90,110],colors='gray')
#f1.show_contour('cii_tdv_2_8.fits',levels=[50],colors='yellow')

f1.show_markers(83.8465208,-4.83829,marker='*',edgecolor='white',facecolor='white',s=200)
f1.add_label(0.4, 0.35, '42 Ori', relative=True, size=12,color='white')
#f1.add_label(0.72, 0.45, 'O9V', relative=True, size=12,color='magenta')
#f1.show_markers(156.01,-57.7,marker='*',edgecolor='magenta',facecolor='magenta',s=100)
#f1.show_markers(156,-57.64,marker='X',edgecolor='red',facecolor='red',alpha=0.5,s=50)
#f1.show_markers(156.,-57.65,marker='X',edgecolor='red',facecolor='red',alpha=1,s=50)
f1.set_xaxis_coord_type('longitude')
f1.set_yaxis_coord_type('latitude')










f2 = aplpy.FITSFigure('rcw120_cii_model_mom_0.fits',north=True,figure =fig,subplot=[0.54,0.1,0.35,0.8])
f2.tick_labels.set_font(size=10)
f2.axis_labels.set_font(size=10)
f2.axis_labels.set_ytext('Dec. (J2000)')
f2.axis_labels.set_xtext('R.A. (J2000)')
f2.show_colorscale(vmin=0,cmap='jet')
f2.add_colorbar(pad=0.3,location='right', axis_label_text="K kms$^{-1}$")
f2.colorbar.set_font(size=10)
f2.add_label(0.2, 0.93, 'RCW 120', relative=True, size=15,color='orangered')
#f1.add_label(0.32, 0.85, '2 to 8 kms$^{-1}$', relative=True, size=15,color='white')
#f1.add_label(0.85, 0.95, 'RCW 120', relative=True, size=15,color='red')
#f1.show_contour('co_tdv_16_22.fits', colors='gray')

f2.set_xaxis_coord_type('scalar')
f2.set_yaxis_coord_type('scalar')

f2.recenter(258.095,-38.45, width=0.24,height=0.235)
#f1.show_contour('rcw49_cii_original.fits',levels=[70,90,110],colors='gray')
#f1.show_contour('cii_tdv_2_8.fits',levels=[50],colors='yellow')
f2.show_markers(258.085,-38.48,marker='*',edgecolor='white',facecolor='white',s=200)
#f1.show_markers(258.10,-38.5,marker='*',edgecolor='magenta',facecolor='magenta',s=200)
f2.add_label(0.65, 0.45, 'CD -38$\degree$11636', relative=True, size=12,color='white')

f2.set_xaxis_coord_type('longitude')
f2.set_yaxis_coord_type('latitude')



f3 =aplpy.FITSFigure('rcw49_cii_model_mom_0.fits',north=True,figure =fig, subplot=[1.08,0.1,0.35,0.8])


#f2.axis_labels.hide()
#f2.tick_labels.hide()
f3.tick_labels.set_font(size=10)
f3.axis_labels.set_font(size=10)
f3.axis_labels.set_ytext('Dec. (J2000)')
f3.axis_labels.set_xtext('R.A. (J2000)')
f3.show_colorscale(vmin=0,cmap='jet')

f3.add_colorbar(pad=0.3,location='right', axis_label_text="K kms$^{-1}$")
f3.colorbar.set_font(size=10)
f3.add_label(0.2, 0.95, 'RCW 49', relative=True, size=15,color='orangered')
#f1.add_label(0.32, 0.85, '2 to 8 kms$^{-1}$', relative=True, size=15,color='white')
#f2.add_label(0.85, 0.95, 'CII @15"', relative=True, size=15,color='red')
#f1.show_contour('co_tdv_16_22.fits', colors='gray')

f3.set_xaxis_coord_type('scalar')
f3.set_yaxis_coord_type('scalar')

f3.recenter(156.045,-57.79, width=0.32,height=0.51)
#f1.show_contour('rcw49_cii_original.fits',levels=[70,90,110],colors='gray')
#f1.show_contour('cii_tdv_2_8.fits',levels=[50],colors='yellow')

f3.show_markers(156.0,-57.755,marker='*',edgecolor='white',facecolor='white',s=200)
f3.add_label(0.6, 0.61, 'Wd2', relative=True, size=12,color='white')
#f1.add_label(0.72, 0.45, 'O9V', relative=True, size=12,color='magenta')
#f1.show_markers(156.01,-57.7,marker='*',edgecolor='magenta',facecolor='magenta',s=100)
#f1.show_markers(156,-57.64,marker='X',edgecolor='red',facecolor='red',alpha=0.5,s=50)
#f1.show_markers(156.,-57.65,marker='X',edgecolor='red',facecolor='red',alpha=1,s=50)
f3.set_xaxis_coord_type('longitude')
f3.set_yaxis_coord_type('latitude')



#f2.save('rcw120_rcw49.png',dpi=300)
f3.save('ngc1977_rcw120_rcw49.png',dpi=300)





