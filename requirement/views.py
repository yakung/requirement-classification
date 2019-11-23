from django.shortcuts import render

from requirement.analysis import RequirementData
from requirement.forms import RequirementForm


def index(request):
    ''' View Method: Index '''
    context = dict()

    if request.method == 'POST':
        form = RequirementForm(request.POST)
        if form.is_valid():
            context['data'] = RequirementData(
                form.cleaned_data.get('title'),
                form.cleaned_data.get('requirements')
            )
            test = request.POST.get('filter')
            context['success'] = "Analysis successful!"
        else:
            context['error'] = form.error
        context['form'] = form
        context['test'] = test
    else:
        context['form'] = RequirementForm()

    # context['data'] = RequirementData('แอปยา', [
    #     'แอปต้องดูรายการยาได้',
    #     'แอปต้องเพิ่มยาได้',
    #     'ต้องล็อกอินได้',
    #     'ต้องดูเวลาทานยาได้',
    #     'ต้องดูรายการหมอได้',
    #     'ต้องดูแผนที่โรงพยาบาลได้',
    #     'ล็อกอินแล้วข้อมูลไม่หาย',
    #     'ล็อกอินแล้วค้างไว้ได้',
    #     'ไม่ทำให้ผู้ใช้หงุดหงิด',
    #     'คลิกรายการโรงพยาบาลแล้วไปที่แผนที่ทันที',
    #     'รองรับกลุ่มผู้ใช้ที่ตาบอดสี',
    #     'ถ้าเป็นฟอนต์ใหญ่ก็ดี',
    #     'ไอคอนเอาไรก็ได้',
    #     'ไม่เอารูปแมงมุมในแอปเด็ดขาด',
    #     'ใส่รูปแมงมุมมาด่านะ',
    #     'ใส่รูปแมงมุมมาลูกค้าไม่เอานะ',
    #     'อยากได้สีฟ้า',
    #     'อยากให้แอปมีรูปไดโนเสาร์ร้องเพลง แต่ถ้าไม่มีไม่เป็นไร',
    #     'ลายก้อนเมฆก็สวยนะ',
    #     'ใส่รูปหมาชิบะก็น่ารักนะ',
    #     'อยากให้เป็นแอปที่ใช้ได้ทุกคน',
    #     'ผู้ใช้ต้องไม่พบปัญหาโหลดนาน',
    #     'เลื่อนขึ้นเลื่อนลงได้',
    #     'ต้องดูชื่อพ่อของหมอได้',
    #     'ต้องดูชื่อแม่ของหมอได้',
    #     'โชว์รายชื่อหมอที่เก่งขึ้นก่อน',
    #     'ปรับเวลาแจ้งเตือนได้',
    #     'เปลี่ยนรูปโปรไฟล์ตัวเองได้',
    #     'รูปเยอะ',
    #     'ไอคอนดูง่ายสบายตา',
    #     'สีสันต้องไม่ฉูดฉาดเดี๋ยวลูกค้าเลิกใช้',
    #     'ไม่เอาแมว',
    #     'เอากะเพราเผ็ด ๆ ไม่ใส่พริก',
    #     'เอาข้าวมันไก่ ใส่เนื้อเป็ด',
    #     'เอาพิซซ่า ไม่ใส่แป้ง',
    #     'ถ้าได้พิซซ่าสีรุ้งก็ดี',
    #     'อยากได้แบบว่าเวลาที่รวดเร็วในการทำงานบางอย่าง',
    #     'อยากได้อะไรที่มันมีสีสันครับ',
    # ])

    return render(request, template_name='requirement/index.html', context=context)
