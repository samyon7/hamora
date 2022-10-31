productName = document.getElementById("product_name")
productCode = document.getElementById("code")
productPrice = document.getElementById("price")
productPriceReal = document.getElementById("real_price")

productName.addEventListener("input", function (event) {
    const {value} = productName

    if (value.length > 1) {
        if (value.split(" ").length === 1) {
             productCode.value = value[0].toUpperCase() + value[1].toUpperCase() + ("00" + lastInput).slice(-3)
        } else if (value.split(" ")[0] !== "" && value.split(" ")[1] !== "") {
            var split = value.split(" ")
            productCode.value = split[0][0].toUpperCase() + split[1][0].toUpperCase() + ("00" + lastInput).slice(-3)
        }
    }
    console.log(productCode.value)
})

let lastInputNumber = ""

productPrice.addEventListener("change", function () {
    const {value} = productPrice
    let clearValue = value
    if(clearValue.includes("Rp. ")){
        clearValue = value.replace("Rp. ", "")
        console.log(clearValue.replaceAll(".", ""))
    }
    if(/^\d+\.\d+$|^\d+$/.test(clearValue)){
        lastInputNumber = formatRupiah(clearValue, "Rp. ")
        productPrice.value = lastInputNumber
        productPriceReal.value = clearValue
    }else if(value == ""){
        productPrice.value = ""
        lastInputNumber = ""
        productPrice.value = ""
    }
    else{
        productPrice.value = lastInputNumber
    }
})

function formatRupiah(angka, prefix){
	var number_string = angka.replace(/[^,\d]/g, '').toString(),
	split   		= number_string.split(','),
	sisa     		= split[0].length % 3,
	rupiah     		= split[0].substr(0, sisa),
	ribuan     		= split[0].substr(sisa).match(/\d{3}/gi);

	// tambahkan titik jika yang di input sudah menjadi angka ribuan
	if(ribuan){
		separator = sisa ? '.' : '';
		rupiah += separator + ribuan.join('.');
	}

	rupiah = split[1] != undefined ? rupiah + ',' + split[1] : rupiah;
	return prefix == undefined ? rupiah : (rupiah ? 'Rp. ' + rupiah : '');
}