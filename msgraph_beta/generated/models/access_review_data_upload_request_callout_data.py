from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_catalog import AccessPackageCatalog
    from .access_package_resource import AccessPackageResource
    from .access_review_instance import AccessReviewInstance
    from .custom_extension_data import CustomExtensionData

from .custom_extension_data import CustomExtensionData

@dataclass
class AccessReviewDataUploadRequestCalloutData(CustomExtensionData, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.accessReviewDataUploadRequestCalloutData"
    # The accessReviewInstance property
    access_review_instance: Optional[AccessReviewInstance] = None
    # The callbackDataType property
    callback_data_type: Optional[str] = None
    # The catalog property
    catalog: Optional[AccessPackageCatalog] = None
    # The resource property
    resource: Optional[AccessPackageResource] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessReviewDataUploadRequestCalloutData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewDataUploadRequestCalloutData
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessReviewDataUploadRequestCalloutData()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_catalog import AccessPackageCatalog
        from .access_package_resource import AccessPackageResource
        from .access_review_instance import AccessReviewInstance
        from .custom_extension_data import CustomExtensionData

        from .access_package_catalog import AccessPackageCatalog
        from .access_package_resource import AccessPackageResource
        from .access_review_instance import AccessReviewInstance
        from .custom_extension_data import CustomExtensionData

        fields: dict[str, Callable[[Any], None]] = {
            "accessReviewInstance": lambda n : setattr(self, 'access_review_instance', n.get_object_value(AccessReviewInstance)),
            "callbackDataType": lambda n : setattr(self, 'callback_data_type', n.get_str_value()),
            "catalog": lambda n : setattr(self, 'catalog', n.get_object_value(AccessPackageCatalog)),
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(AccessPackageResource)),
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
        writer.write_object_value("accessReviewInstance", self.access_review_instance)
        writer.write_str_value("callbackDataType", self.callback_data_type)
        writer.write_object_value("catalog", self.catalog)
        writer.write_object_value("resource", self.resource)
    

