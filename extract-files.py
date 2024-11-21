#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    "vendor/oneplus/sm8450-common",
    "hardware/oplus",
    "hardware/qcom-caf/sm8450",
    "vendor/qcom/opensource/commonsys/display",
    "device/oneplus/sm8450-common",
    "hardware/qcom-caf/sm8450/audio/agm/ipc/HwBinders/legacy",
    "hardware/qcom-caf/wlan",
    "vendor/qcom/opensource/commonsys-intf/display",
    "vendor/qcom/opensource/dataservices",
]

blob_fixups: blob_fixups_user_type = {
    'odm/lib64/libAlgoProcess.so': blob_fixup()
        .replace_needed('android.hardware.graphics.common-V2-ndk_platform.so', 'android.hardware.graphics.common-V5-ndk.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    "ovaltine",
    "oneplus",
    namespace_imports=namespace_imports,
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
)

if __name__ == "__main__":
    utils = ExtractUtils.device_with_common(module, "sm8450-common", module.vendor)
    utils.run()
