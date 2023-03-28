from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_package_custom_extension_stage, custom_callout_extension, entity

from . import entity

class CustomExtensionStageSetting(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new customExtensionStageSetting and sets the default values.
        """
        super().__init__()
        # Indicates the custom workflow extension that will be executed at this stage. Nullable. Supports $expand.
        self._custom_extension: Optional[custom_callout_extension.CustomCalloutExtension] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The stage property
        self._stage: Optional[access_package_custom_extension_stage.AccessPackageCustomExtensionStage] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustomExtensionStageSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CustomExtensionStageSetting
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CustomExtensionStageSetting()
    
    @property
    def custom_extension(self,) -> Optional[custom_callout_extension.CustomCalloutExtension]:
        """
        Gets the customExtension property value. Indicates the custom workflow extension that will be executed at this stage. Nullable. Supports $expand.
        Returns: Optional[custom_callout_extension.CustomCalloutExtension]
        """
        return self._custom_extension
    
    @custom_extension.setter
    def custom_extension(self,value: Optional[custom_callout_extension.CustomCalloutExtension] = None) -> None:
        """
        Sets the customExtension property value. Indicates the custom workflow extension that will be executed at this stage. Nullable. Supports $expand.
        Args:
            value: Value to set for the custom_extension property.
        """
        self._custom_extension = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_package_custom_extension_stage, custom_callout_extension, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "customExtension": lambda n : setattr(self, 'custom_extension', n.get_object_value(custom_callout_extension.CustomCalloutExtension)),
            "stage": lambda n : setattr(self, 'stage', n.get_enum_value(access_package_custom_extension_stage.AccessPackageCustomExtensionStage)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("customExtension", self.custom_extension)
        writer.write_enum_value("stage", self.stage)
    
    @property
    def stage(self,) -> Optional[access_package_custom_extension_stage.AccessPackageCustomExtensionStage]:
        """
        Gets the stage property value. The stage property
        Returns: Optional[access_package_custom_extension_stage.AccessPackageCustomExtensionStage]
        """
        return self._stage
    
    @stage.setter
    def stage(self,value: Optional[access_package_custom_extension_stage.AccessPackageCustomExtensionStage] = None) -> None:
        """
        Sets the stage property value. The stage property
        Args:
            value: Value to set for the stage property.
        """
        self._stage = value
    

