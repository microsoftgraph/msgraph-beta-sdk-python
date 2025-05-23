from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .update_category_enrollment_information import UpdateCategoryEnrollmentInformation

@dataclass
class UpdateManagementEnrollment(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The driver property
    driver: Optional[UpdateCategoryEnrollmentInformation] = None
    # The feature property
    feature: Optional[UpdateCategoryEnrollmentInformation] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The quality property
    quality: Optional[UpdateCategoryEnrollmentInformation] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UpdateManagementEnrollment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpdateManagementEnrollment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UpdateManagementEnrollment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .update_category_enrollment_information import UpdateCategoryEnrollmentInformation

        from .update_category_enrollment_information import UpdateCategoryEnrollmentInformation

        fields: dict[str, Callable[[Any], None]] = {
            "driver": lambda n : setattr(self, 'driver', n.get_object_value(UpdateCategoryEnrollmentInformation)),
            "feature": lambda n : setattr(self, 'feature', n.get_object_value(UpdateCategoryEnrollmentInformation)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "quality": lambda n : setattr(self, 'quality', n.get_object_value(UpdateCategoryEnrollmentInformation)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("driver", self.driver)
        writer.write_object_value("feature", self.feature)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("quality", self.quality)
        writer.write_additional_data_value(self.additional_data)
    

