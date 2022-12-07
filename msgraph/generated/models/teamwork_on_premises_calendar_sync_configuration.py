from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class TeamworkOnPremisesCalendarSyncConfiguration(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new teamworkOnPremisesCalendarSyncConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The fully qualified domain name (FQDN) of the Skype for Business Server. Use the Exchange domain if the Skype for Business SIP domain is different from the Exchange domain of the user.
        self._domain: Optional[str] = None
        # The domain and username of the console device, for example, Seattle/RanierConf.
        self._domain_user_name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The Simple Mail Transfer Protocol (SMTP) address of the user account. This is only required if a different user principal name (UPN) is used to sign in to Exchange other than Microsoft Teams and Skype for Business. This is a common scenario in a hybrid environment where an on-premises Exchange server is used.
        self._smtp_address: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkOnPremisesCalendarSyncConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkOnPremisesCalendarSyncConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkOnPremisesCalendarSyncConfiguration()
    
    @property
    def domain(self,) -> Optional[str]:
        """
        Gets the domain property value. The fully qualified domain name (FQDN) of the Skype for Business Server. Use the Exchange domain if the Skype for Business SIP domain is different from the Exchange domain of the user.
        Returns: Optional[str]
        """
        return self._domain
    
    @domain.setter
    def domain(self,value: Optional[str] = None) -> None:
        """
        Sets the domain property value. The fully qualified domain name (FQDN) of the Skype for Business Server. Use the Exchange domain if the Skype for Business SIP domain is different from the Exchange domain of the user.
        Args:
            value: Value to set for the domain property.
        """
        self._domain = value
    
    @property
    def domain_user_name(self,) -> Optional[str]:
        """
        Gets the domainUserName property value. The domain and username of the console device, for example, Seattle/RanierConf.
        Returns: Optional[str]
        """
        return self._domain_user_name
    
    @domain_user_name.setter
    def domain_user_name(self,value: Optional[str] = None) -> None:
        """
        Sets the domainUserName property value. The domain and username of the console device, for example, Seattle/RanierConf.
        Args:
            value: Value to set for the domainUserName property.
        """
        self._domain_user_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "domain": lambda n : setattr(self, 'domain', n.get_str_value()),
            "domain_user_name": lambda n : setattr(self, 'domain_user_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "smtp_address": lambda n : setattr(self, 'smtp_address', n.get_str_value()),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("domain", self.domain)
        writer.write_str_value("domainUserName", self.domain_user_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("smtpAddress", self.smtp_address)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def smtp_address(self,) -> Optional[str]:
        """
        Gets the smtpAddress property value. The Simple Mail Transfer Protocol (SMTP) address of the user account. This is only required if a different user principal name (UPN) is used to sign in to Exchange other than Microsoft Teams and Skype for Business. This is a common scenario in a hybrid environment where an on-premises Exchange server is used.
        Returns: Optional[str]
        """
        return self._smtp_address
    
    @smtp_address.setter
    def smtp_address(self,value: Optional[str] = None) -> None:
        """
        Sets the smtpAddress property value. The Simple Mail Transfer Protocol (SMTP) address of the user account. This is only required if a different user principal name (UPN) is used to sign in to Exchange other than Microsoft Teams and Skype for Business. This is a common scenario in a hybrid environment where an on-premises Exchange server is used.
        Args:
            value: Value to set for the smtpAddress property.
        """
        self._smtp_address = value
    

