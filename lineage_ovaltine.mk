#
# Copyright (C) 2021-2023 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit from ovaltine device
$(call inherit-product, device/oneplus/ovaltine/device.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

PRODUCT_NAME := lineage_ovaltine
PRODUCT_DEVICE := ovaltine
PRODUCT_MANUFACTURER := OnePlus
PRODUCT_BRAND := OnePlus
PRODUCT_MODEL := CPH2417

PRODUCT_GMS_CLIENTID_BASE := android-oneplus

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="qssi-user 14 UKQ1.230924.001 1725609152768 release-keys" \
    BuildFingerprint=OnePlus/CPH2417/OP5552L1:13/SKQ1.221119.001/S.19e9506-35-25b49:user/release-keys \
    DeviceName=OnePlus10T \
    DeviceProduct=OnePlus10T \
    SystemName=CPH2417 \
    SystemDevice=OP5552L1
