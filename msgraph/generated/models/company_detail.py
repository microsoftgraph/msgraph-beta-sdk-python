from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

physical_address = lazy_import('msgraph.generated.models.physical_address')

class CompanyDetail(AdditionalDataHolder, Parsable):
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
    def address(self,) -> Optional[physical_address.PhysicalAddress]:
        """
        Gets the address property value. Address of the company.
        Returns: Optional[physical_address.PhysicalAddress]
        """
        return self._address
    
    @address.setter
    def address(self,value: Optional[physical_address.PhysicalAddress] = None) -> None:
        """
        Sets the address property value. Address of the company.
        Args:
            value: Value to set for the address property.
        """
        self._address = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new companyDetail and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Address of the company.
        self._address: Optional[physical_address.PhysicalAddress] = None
        # Department Name within a company.
        self._department: Optional[str] = None
        # Company name.
        self._display_name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Office Location of the person referred to.
        self._office_location: Optional[str] = None
        # Pronunciation guide for the company name.
        self._pronunciation: Optional[str] = None
        # Link to the company home page.
        self._web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CompanyDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CompanyDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CompanyDetail()
    
    @property
    def department(self,) -> Optional[str]:
        """
        Gets the department property value. Department Name within a company.
        Returns: Optional[str]
        """
        return self._department
    
    @department.setter
    def department(self,value: Optional[str] = None) -> None:
        """
        Sets the department property value. Department Name within a company.
        Args:
            value: Value to set for the department property.
        """
        self._department = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Company name.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Company name.
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
            "address": lambda n : setattr(self, 'address', n.get_object_value(physical_address.PhysicalAddress)),
            "department": lambda n : setattr(self, 'department', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "office_location": lambda n : setattr(self, 'office_location', n.get_str_value()),
            "pronunciation": lambda n : setattr(self, 'pronunciation', n.get_str_value()),
            "web_url": lambda n : setattr(self, 'web_url', n.get_str_value()),
        }
        return fields
    
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
    
    @property
    def office_location(self,) -> Optional[str]:
        """
        Gets the officeLocation property value. Office Location of the person referred to.
        Returns: Optional[str]
        """
        return self._office_location
    
    @office_location.setter
    def office_location(self,value: Optional[str] = None) -> None:
        """
        Sets the officeLocation property value. Office Location of the person referred to.
        Args:
            value: Value to set for the officeLocation property.
        """
        self._office_location = value
    
    @property
    def pronunciation(self,) -> Optional[str]:
        """
        Gets the pronunciation property value. Pronunciation guide for the company name.
        Returns: Optional[str]
        """
        return self._pronunciation
    
    @pronunciation.setter
    def pronunciation(self,value: Optional[str] = None) -> None:
        """
        Sets the pronunciation property value. Pronunciation guide for the company name.
        Args:
            value: Value to set for the pronunciation property.
        """
        self._pronunciation = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("address", self.address)
        writer.write_str_value("department", self.department)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("officeLocation", self.office_location)
        writer.write_str_value("pronunciation", self.pronunciation)
        writer.write_str_value("webUrl", self.web_url)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def web_url(self,) -> Optional[str]:
        """
        Gets the webUrl property value. Link to the company home page.
        Returns: Optional[str]
        """
        return self._web_url
    
    @web_url.setter
    def web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the webUrl property value. Link to the company home page.
        Args:
            value: Value to set for the webUrl property.
        """
        self._web_url = value
    

