from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

management_category = lazy_import('msgraph.generated.models.managed_tenants.management_category')

class ManagementTemplateDetailedInfo(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def category(self,) -> Optional[management_category.ManagementCategory]:
        """
        Gets the category property value. The category property
        Returns: Optional[management_category.ManagementCategory]
        """
        return self._category
    
    @category.setter
    def category(self,value: Optional[management_category.ManagementCategory] = None) -> None:
        """
        Sets the category property value. The category property
        Args:
            value: Value to set for the category property.
        """
        self._category = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new managementTemplateDetailedInfo and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The category property
        self._category: Optional[management_category.ManagementCategory] = None
        # The display name for the management template. Required. Read-only.
        self._display_name: Optional[str] = None
        # The unique identifier for the management template. Required. Read-only.
        self._management_template_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The version property
        self._version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagementTemplateDetailedInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagementTemplateDetailedInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagementTemplateDetailedInfo()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the management template. Required. Read-only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the management template. Required. Read-only.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "category": lambda n : setattr(self, 'category', n.get_enum_value(management_category.ManagementCategory)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "management_template_id": lambda n : setattr(self, 'management_template_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
        }
        return fields
    
    @property
    def management_template_id(self,) -> Optional[str]:
        """
        Gets the managementTemplateId property value. The unique identifier for the management template. Required. Read-only.
        Returns: Optional[str]
        """
        return self._management_template_id
    
    @management_template_id.setter
    def management_template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the managementTemplateId property value. The unique identifier for the management template. Required. Read-only.
        Args:
            value: Value to set for the managementTemplateId property.
        """
        self._management_template_id = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("category", self.category)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("managementTemplateId", self.management_template_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("version", self.version)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def version(self,) -> Optional[int]:
        """
        Gets the version property value. The version property
        Returns: Optional[int]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[int] = None) -> None:
        """
        Sets the version property value. The version property
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

