from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_gallery_image_status import CloudPcGalleryImageStatus
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPcGalleryImage(Entity, Parsable):
    # The display name of this gallery image. For example, Windows 11 Enterprise + Microsoft 365 Apps 22H2. Read-only.
    display_name: Optional[str] = None
    # The date when the status of image becomes supportedWithWarning. Users can still provision new Cloud PCs if the current time is later than endDate and earlier than expirationDate. For example, assume the endDate of a gallery image is 2023-9-14 and expirationDate is 2024-3-14, users are able to provision new Cloud PCs if today is 2023-10-01. Read-only.
    end_date: Optional[datetime.date] = None
    # The date when the image is no longer available. Users are unable to provision new Cloud PCs if the current time is later than expirationDate. The value is usually endDate plus six months. For example, if the startDate is 2025-10-14, the expirationDate is usually 2026-04-14. Read-only.
    expiration_date: Optional[datetime.date] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The offer name of this gallery image that is passed to ARM to retrieve the image resource. Read-only. The offer property is deprecated and will stop returning data on January 31, 2024. Going forward, use the offerName property.
    offer: Optional[str] = None
    # The official display offer name of this gallery image. For example, Windows 10 Enterprise + OS Optimizations. The offerDisplayName property is deprecated and will stop returning data on January 31, 2024.
    offer_display_name: Optional[str] = None
    # The offer name of this gallery image that is passed to ARM to retrieve the image resource. Read-only.
    offer_name: Optional[str] = None
    # The operating system version of this gallery image. For example, 10.0.22000.296. Read-only.
    os_version_number: Optional[str] = None
    # The publisher name of this gallery image that is passed to ARM to retrieve the image resource. Read-only. The publisher property is deprecated and will stop returning data on January 31, 2024. Going forward, use the publisherName property.
    publisher: Optional[str] = None
    # The publisher name of this gallery image that is passed to ARM to retrieve the image resource. Read-only.
    publisher_name: Optional[str] = None
    # The recommended Cloud PC SKU for this gallery image. Read-only. The recommendedSku property is deprecated and will stop returning data on January 31, 2024.
    recommended_sku: Optional[str] = None
    # Indicates the size of this image in gigabytes. For example, 64. Read-only.
    size_in_g_b: Optional[int] = None
    # The SKU name of this image that is passed to ARM to retrieve the image resource. Read-only. The sku property is deprecated and will stop returning data on January 31, 2024. Going forward, use the skuName property.
    sku: Optional[str] = None
    # The official display SKU name of this gallery image. For example, 2004. Read-only. The skuDisplayName property is deprecated and will stop returning data on January 31, 2024.
    sku_display_name: Optional[str] = None
    # The SKU name of this image that is passed to ARM to retrieve the image resource. Read-only.
    sku_name: Optional[str] = None
    # The date when the Cloud PC image is available for provisioning new Cloud PCs. For example, 2022-09-20. Read-only.
    start_date: Optional[datetime.date] = None
    # The status of the gallery image on the Cloud PC. Possible values are: supported, supportedWithWarning, notSupported, unknownFutureValue. The default value is supported. Read-only.
    status: Optional[CloudPcGalleryImageStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcGalleryImage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcGalleryImage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcGalleryImage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_gallery_image_status import CloudPcGalleryImageStatus
        from .entity import Entity

        from .cloud_pc_gallery_image_status import CloudPcGalleryImageStatus
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "endDate": lambda n : setattr(self, 'end_date', n.get_date_value()),
            "expirationDate": lambda n : setattr(self, 'expiration_date', n.get_date_value()),
            "offer": lambda n : setattr(self, 'offer', n.get_str_value()),
            "offerDisplayName": lambda n : setattr(self, 'offer_display_name', n.get_str_value()),
            "offerName": lambda n : setattr(self, 'offer_name', n.get_str_value()),
            "osVersionNumber": lambda n : setattr(self, 'os_version_number', n.get_str_value()),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
            "publisherName": lambda n : setattr(self, 'publisher_name', n.get_str_value()),
            "recommendedSku": lambda n : setattr(self, 'recommended_sku', n.get_str_value()),
            "sizeInGB": lambda n : setattr(self, 'size_in_g_b', n.get_int_value()),
            "sku": lambda n : setattr(self, 'sku', n.get_str_value()),
            "skuDisplayName": lambda n : setattr(self, 'sku_display_name', n.get_str_value()),
            "skuName": lambda n : setattr(self, 'sku_name', n.get_str_value()),
            "startDate": lambda n : setattr(self, 'start_date', n.get_date_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(CloudPcGalleryImageStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_date_value("endDate", self.end_date)
        writer.write_date_value("expirationDate", self.expiration_date)
        writer.write_str_value("offer", self.offer)
        writer.write_str_value("offerDisplayName", self.offer_display_name)
        writer.write_str_value("offerName", self.offer_name)
        writer.write_str_value("osVersionNumber", self.os_version_number)
        writer.write_str_value("publisher", self.publisher)
        writer.write_str_value("publisherName", self.publisher_name)
        writer.write_str_value("recommendedSku", self.recommended_sku)
        writer.write_int_value("sizeInGB", self.size_in_g_b)
        writer.write_str_value("sku", self.sku)
        writer.write_str_value("skuDisplayName", self.sku_display_name)
        writer.write_str_value("skuName", self.sku_name)
        writer.write_date_value("startDate", self.start_date)
        writer.write_enum_value("status", self.status)
    

